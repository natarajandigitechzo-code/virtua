// Vercel Serverless Function: proxies lead submissions to the Virtua Connect
// public leads API. Keeps VIRTUA_LEADS_API_KEY server-side only — never sent
// to the browser.

const LEADS_ENDPOINT = 'https://api.virtuaconnect.virtuagrid.com/api/public/leads/submit';

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const apiKey = process.env.VIRTUA_LEADS_API_KEY;
  if (!apiKey) {
    console.error('submit-lead: VIRTUA_LEADS_API_KEY is not set');
    return res.status(500).json({ message: 'Lead submission is not configured' });
  }

  const body = req.body || {};
  const name = typeof body.name === 'string' ? body.name.trim() : '';

  if (!name) {
    return res.status(400).json({ message: 'name is required' });
  }

  // Only forward the fields the public API accepts, trimmed of empties.
  const payload = { name };
  for (const field of ['email', 'countryCode', 'phoneNumber', 'phone', 'notes']) {
    const val = body[field];
    if (typeof val === 'string' && val.trim()) payload[field] = val.trim();
  }

  try {
    const upstream = await fetch(LEADS_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-project-api-key': apiKey,
      },
      body: JSON.stringify(payload),
    });

    const data = await upstream.json().catch(() => ({}));
    return res.status(upstream.status).json(data);
  } catch (err) {
    console.error('submit-lead: upstream request failed', err);
    return res.status(502).json({ message: 'Failed to reach lead service' });
  }
};

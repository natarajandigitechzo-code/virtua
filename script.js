// Virtua Technologies Interactive Mechanics & ROI Calculator

document.addEventListener('DOMContentLoaded', () => {

  // Interactive Screen Tab Switcher
  const tabBtns = document.querySelectorAll('.tab-btn');
  const screenViews = document.querySelectorAll('.screen-view');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetView = btn.getAttribute('data-view');

      tabBtns.forEach(b => b.classList.remove('active'));
      screenViews.forEach(v => v.classList.remove('active'));

      btn.classList.add('active');
      const activeScreen = document.getElementById(`view-${targetView}`);
      if (activeScreen) activeScreen.classList.add('active');
    });
  });

  // Interactive ROI Calculator Logic
  const rangeAsset = document.getElementById('range-asset');
  const rangeVol = document.getElementById('range-vol');
  const rangeClients = document.getElementById('range-clients');

  const calcAssetVal = document.getElementById('calc-asset-val');
  const calcVolVal = document.getElementById('calc-vol-val');
  const calcClientsVal = document.getElementById('calc-clients-val');

  const calcTotal = document.getElementById('calc-total');
  const cbListing = document.getElementById('cb-listing');
  const cbTrading = document.getElementById('cb-trading');
  const cbSaas = document.getElementById('cb-saas');

  function formatMoney(num) {
    return '$' + num.toLocaleString('en-US');
  }

  function updateCalculator() {
    if (!rangeAsset || !rangeVol || !rangeClients) return;

    const assetVal = parseInt(rangeAsset.value);
    const volVal = parseInt(rangeVol.value);
    const clientsCount = parseInt(rangeClients.value);

    calcAssetVal.textContent = formatMoney(assetVal);
    calcVolVal.textContent = formatMoney(volVal);
    calcClientsVal.textContent = `${clientsCount} Issuers`;

    // Revenue calculations: 1.5% listing fee + 2% trading commission + $10,000/yr per SaaS issuer client
    const listingRevenue = Math.round(assetVal * 0.015);
    const tradingRevenue = Math.round(volVal * 0.02);
    const saasRevenue = Math.round(clientsCount * 17500);

    const totalRev = listingRevenue + tradingRevenue + saasRevenue;

    cbListing.textContent = formatMoney(listingRevenue);
    cbTrading.textContent = formatMoney(tradingRevenue);
    cbSaas.textContent = formatMoney(saasRevenue);
    calcTotal.textContent = formatMoney(totalRev);
  }

  if (rangeAsset) {
    rangeAsset.addEventListener('input', updateCalculator);
    rangeVol.addEventListener('input', updateCalculator);
    rangeClients.addEventListener('input', updateCalculator);
    updateCalculator();
  }

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isActive) item.classList.add('active');
    });
  });

  // Modal Dialog Logic
  const modalOverlay = document.getElementById('modal-overlay');
  const openModalBtns = document.querySelectorAll('.open-modal');
  const closeModalBtn = document.getElementById('modal-close');
  const successCloseBtn = document.getElementById('success-close');
  const leadForm = document.getElementById('lead-form');
  const modalSuccess = document.getElementById('modal-success');

  // Tracks which CTA button opened the modal, so the lead submission can
  // tell the CRM apart (e.g. "Live Demo" click vs "Strategy Call" click).
  let activeCtaSource = 'Strategy Call';

  const openModal = () => {
    modalOverlay.classList.add('active');
  };

  const closeModal = () => {
    modalOverlay.classList.remove('active');
    setTimeout(() => {
      if (leadForm) {
        leadForm.style.display = 'flex';
        modalSuccess.classList.remove('active');
        leadForm.reset();
      }
    }, 300);
  };

  openModalBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      activeCtaSource = btn.dataset.ctaSource || btn.querySelector('span')?.textContent.trim() || 'CTA';
      openModal();
    });
  });

  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
  if (successCloseBtn) successCloseBtn.addEventListener('click', closeModal);

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });
  }

  // Form Submit — posts to our serverless proxy (/api/submit-lead), which
  // holds the CRM API key server-side and forwards to Virtua Connect.
  if (leadForm) {
    const submitBtn = document.getElementById('lead-submit-btn');
    const errorEl = document.getElementById('lead-form-error');

    const showError = (msg) => {
      if (!errorEl) return;
      errorEl.textContent = msg;
      errorEl.style.display = 'block';
    };
    const clearError = () => {
      if (!errorEl) return;
      errorEl.style.display = 'none';
      errorEl.textContent = '';
    };

    leadForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearError();

      const name = document.getElementById('lead-name')?.value.trim();
      const email = document.getElementById('lead-email')?.value.trim();
      const countryCode = document.getElementById('lead-country-code')?.value.trim();
      const phoneNumber = document.getElementById('lead-phone')?.value.trim();
      const assetClass = document.getElementById('lead-asset-class')?.value;

      if (!name || !email) {
        showError('Please fill in your name and work email.');
        return;
      }

      const notesParts = [`Source: ${activeCtaSource}`];
      if (assetClass) notesParts.push(`Asset Class: ${assetClass}`);

      const payload = {
        name,
        email,
        notes: notesParts.join(' | '),
      };
      if (countryCode) payload.countryCode = countryCode;
      if (phoneNumber) payload.phoneNumber = phoneNumber;
      if (countryCode && phoneNumber) payload.phone = `${countryCode}${phoneNumber}`;

      submitBtn?.classList.add('is-loading');
      if (submitBtn) submitBtn.disabled = true;

      try {
        const res = await fetch('/api/submit-lead', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });

        if (!res.ok) {
          const errBody = await res.json().catch(() => ({}));
          throw new Error(errBody.message || `Request failed (${res.status})`);
        }

        leadForm.style.display = 'none';
        modalSuccess.classList.add('active');
      } catch (err) {
        showError(err.message || 'Something went wrong. Please try again.');
      } finally {
        submitBtn?.classList.remove('is-loading');
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  }

  // Buy Fractional Shares Button Listener
  const dashInvestBtns = document.querySelectorAll('.btn-dash-invest');
  dashInvestBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const cardTitle = e.target.closest('.dash-card-hover')?.querySelector('h4')?.innerText || 'Asset Shares';
      showToast(`Processing Smart Contract Order for 1 Share of ${cardTitle}...`);
      setTimeout(() => {
        showToast(`Transaction Confirmed! You now own 1 Fractional Share of ${cardTitle}.`);
      }, 1200);
    });
  });

  // Interactive Mint Token Simulator
  const btnSimulateMint = document.getElementById('btnSimulateMint');
  if (btnSimulateMint) {
    btnSimulateMint.addEventListener('click', () => {
      const val = document.getElementById('simValuation')?.value || '10,000,000';
      const frac = document.getElementById('simFraction')?.value || '500';
      showToast(`Minting Smart Contract for $${Number(val).toLocaleString()} Valuation ($${frac}/fraction)...`);

      setTimeout(() => {
        showToast(`Success! ERC-3643 Token Contract Deployed Live on EVM Mainnet!`);
      }, 1500);
    });
  }

  function showToast(msg) {
    let t = document.createElement('div');
    t.style.position = 'fixed';
    t.style.bottom = '24px';
    t.style.right = '24px';
    t.style.background = 'linear-gradient(135deg, #F59E0B, #D97706)';
    t.style.color = '#000';
    t.style.padding = '12px 22px';
    t.style.borderRadius = '12px';
    t.style.fontWeight = '800';
    t.style.fontSize = '0.9rem';
    t.style.boxShadow = '0 10px 30px rgba(0,0,0,0.6)';
    t.style.zIndex = '99999';
    t.style.transition = 'all 0.3s ease';
    t.innerText = msg;
    document.body.appendChild(t);

    setTimeout(() => {
      t.style.opacity = '0';
      t.style.transform = 'translateY(10px)';
      setTimeout(() => t.remove(), 300);
    }, 3000);
  }

});

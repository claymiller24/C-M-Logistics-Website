// Small front-end handler for the contact form. Validates and provides a mailto fallback.
document.addEventListener('DOMContentLoaded', function(){
  const yearEl = document.getElementById('year');
  if(yearEl) yearEl.textContent = new Date().getFullYear();

  const form = document.getElementById('contactForm');
  const result = document.getElementById('formResult');
  if(!form) return;

  form.addEventListener('submit', function(e){
    e.preventDefault();
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const message = form.message.value.trim();
    result.textContent = '';

    if(!name || !email || !message){
      result.textContent = 'Please fill out all fields.';
      return;
    }

    // Try to use fetch to submit to an API endpoint if configured (not provided here).
    // Fallback: open mail client via mailto
    const subject = encodeURIComponent('Website inquiry from ' + name);
    const body = encodeURIComponent(message + '\n\n— ' + name + ' (' + email + ')');
  const mailto = 'mailto:millerclay46@gmail.com?subject=' + subject + '&body=' + body;

    // Show a friendly message and open mail client
    result.textContent = 'Opening your mail client...';
    window.location.href = mailto;
  });
});

// Register Service Worker for offline support and install prompts
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function(){
    navigator.serviceWorker.register('/sw.js').catch(function(err){
      // no-op: SW registration failed (likely local file or unsupported)
    });
  });
}

// Lightweight PWA install button when supported
(function(){
  let deferredPrompt = null;
  function addInstallButton(){
    if (!document.body) {
      window.addEventListener('DOMContentLoaded', addInstallButton, { once: true });
      return;
    }
    const btn = document.createElement('button');
    btn.textContent = 'Install App';
    btn.setAttribute('aria-label', 'Install this app');
    btn.style.position = 'fixed';
    btn.style.bottom = '16px';
    btn.style.right = '16px';
    btn.style.zIndex = '10000';
    btn.style.padding = '10px 14px';
    btn.style.background = '#0f1624';
    btn.style.color = '#fff';
    btn.style.border = 'none';
    btn.style.borderRadius = '6px';
    btn.style.boxShadow = '0 2px 6px rgba(0,0,0,.2)';
    btn.style.cursor = 'pointer';
    btn.addEventListener('click', function(){
      if (!deferredPrompt) return;
      btn.disabled = true;
      deferredPrompt.prompt();
      deferredPrompt.userChoice.finally(function(){
        btn.remove();
        deferredPrompt = null;
      });
    });
    document.body.appendChild(btn);
  }

  window.addEventListener('beforeinstallprompt', function(e){
    e.preventDefault();
    deferredPrompt = e;
    addInstallButton();
  });
})();

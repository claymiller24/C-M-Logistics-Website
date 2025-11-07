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

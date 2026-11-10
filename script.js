(() => {
  const button = document.getElementById('language');
  const elements = document.querySelectorAll('[data-en][data-zh]');
  button.hidden = false;
  button.addEventListener('click', () => {
    const language = document.documentElement.lang === 'en' ? 'zh' : 'en';
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    elements.forEach(element => { element.textContent = element.dataset[language]; });
    button.textContent = language === 'en' ? '中文' : 'English';
    button.setAttribute('aria-label', language === 'en' ? 'Switch to Chinese' : 'Switch to English');
    document.querySelector('nav').setAttribute('aria-label', language === 'en' ? 'Main navigation' : '主导航');
    document.querySelector('.wordmark').setAttribute('aria-label', language === 'en' ? 'Home' : '首页');
  });
})();

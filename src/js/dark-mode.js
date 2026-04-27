(function(){
  var toggle=document.getElementById('theme-toggle');
  if(!toggle)return;
  var theme=localStorage.getItem('ctw-theme');
  if(theme)document.documentElement.setAttribute('data-theme',theme);
  toggle.addEventListener('click',function(){
    var current=document.documentElement.getAttribute('data-theme');
    var next=current==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',next);
    localStorage.setItem('ctw-theme',next);
    toggle.textContent=next==='dark'?'☀':'☾';
  });
  if(theme==='dark')toggle.textContent='☀';
})();
function toggleMenu(){
  const menu   = document.getElementById("userMenu");
  const back   = document.getElementById("menuBackdrop");
  menu.classList.toggle("open");
  back.classList.toggle("active");
}

document.addEventListener('click', e=>{
  const menu = document.getElementById("userMenu");
  const back = document.getElementById("menuBackdrop");
  const avatar = document.querySelector('.user-avatar');
  if(menu && !menu.contains(e.target) && !avatar.contains(e.target)){
    menu.classList.remove("open");
    back.classList.remove("active");
  }
});
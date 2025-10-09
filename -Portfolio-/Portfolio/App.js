const hotdog = document.querySelector('.upper .nav-bar .nav-list .hotdog');
const mobile_menu = document.querySelector('.upper .nav-bar .nav-list ul');
const menu_item = document.querySelectorAll('.upper .nav-bar .nav-list ul li a');
const header = document.querySelector('.upper.container');

hotdog.addEventListener('click',()=>{
    hotdog.classList.toggle('active');
    mobile_menu.classList.toggle('active');
});

document.addEventListener('scroll',()=>{
    var scroll_position = window.scrollY;
    if(scroll_position > 350){
        header.style.backgroundColor = 'rgb(54, 56, 54)';
        header.classList.add('scrolled');
    }else{
        header.style.backgroundColor = '#82ABBA';
        header.classList.remove('scrolled');
    }
});

menu_item.forEach(item=>{
    item.addEventListener('click',()=>{
        hotdog.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    });
});

const photoStack = document.querySelector('.photo-stack');

if (photoStack) {
  photoStack.addEventListener('click', (event) => {
    const clickedPhoto = event.target.closest('.photo');

    if (!clickedPhoto || !clickedPhoto.classList.contains('preview')) { 
      return;
    }

    const photos = Array.from(photoStack.querySelectorAll('.photo'));
    const main = photoStack.querySelector('.photo.main');
    const preview = photoStack.querySelector('.photo.preview');

    const hiddenList = photos.filter(p => !p.classList.contains('main') && !p.classList.contains('preview'));
    const nextHidden = hiddenList[0];

    if (!main || !preview || !nextHidden) return;

    main.classList.remove('main');
    main.classList.add('hidden');

    preview.classList.remove('preview');
    preview.classList.add('main');

    nextHidden.classList.remove('hidden');
    nextHidden.classList.add('preview');

    photoStack.appendChild(main);
  });
}


(function () {

    let profileBtn = document.querySelector('.header-content [class=profile-button]');

    let profileMenu = document.querySelector('.header-content [class=profile-menu]');

    profileBtn.addEventListener('click', function() {
        profileMenu.classList.toggle("--active");
    });

    let MainField = document.getElementsByTagName('main');

    MainField[0].addEventListener('click', function(e) {
        let targetItem = e.target;
        if (targetItem.closest(".selector")) {
            let Parent = targetItem.closest(".selector");
            if (Parent.childNodes[1].style.fill === "none") {
                Parent.childNodes[1].style.fill = "red";
            } else {
                Parent.childNodes[1].style.fill = "none";
            }
        }
    });
})();

function previewImage() {
            var previewContainer = document.getElementById('preview-container');
            var previewImage = document.getElementById('preview-image');
            var fileInput = document.getElementById('image-input');
            var file = fileInput.files[0];

            if (file) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = 'block';
                };

                reader.readAsDataURL(file);
            } else {
                previewImage.src = '#';
                previewImage.style.display = 'none';
            }
        }
function previewAva() {
            var previewContainer = document.getElementById('ava-preview-container');
            var previewImage = document.getElementById('ava-preview-image');
            var fileInput = document.getElementById('ava-input');
            var file = fileInput.files[0];

            if (file) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = 'block';
                };

                reader.readAsDataURL(file);
            } else {
                previewImage.src = '#';
                previewImage.style.display = 'none';
            }
        }

function previewPostEdit(e) {
	    console.log(e.target);
            var previewContainer = document.getElementById('ava-preview-container');
            var previewImage = document.getElementById('ava-preview-image');
            var fileInput = document.getElementById('ava-input');
            var file = fileInput.files[0];

            if (file) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = 'block';
                };

                reader.readAsDataURL(file);
            } else {
                previewImage.src = '#';
                previewImage.style.display = 'none';
            }
        }

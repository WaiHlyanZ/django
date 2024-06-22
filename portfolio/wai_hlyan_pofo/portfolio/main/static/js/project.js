let slideIndex = 1;
showSlides(slideIndex)

function moveSlide(n) {
    slideIndex += n
    showSlides(slideIndex)
}

// Show only the image that are in the current index: `n`
function showSlides(n) {
    let slides = document.getElementsByClassName("carousel-item")
    // Go to the first
    if (n > slides.length) {
        slideIndex = 1
    }
    // Go to the last
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"
    }
    slides[slideIndex - 1].style.display = "flex"
}
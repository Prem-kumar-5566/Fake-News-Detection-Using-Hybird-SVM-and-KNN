// window.onload = function() {
//     document.getElementById('textOverlay').style.left = '20%';
//     var imagePopout = document.getElementById("imagePopout");
//     imagePopout.style.transform = "translate(-50%, -50%) scale(1)";
// };


window.onload = function() {
    document.getElementById('textOverlay').style.left = '20%';
    var imagePopout = document.getElementById("imagePopout");
    imagePopout.style.transform = "translate(-50%, -50%) scale(1)";
    
    // Show the dynamic textbox with fade-in effect
    var dynamicTextbox = document.getElementById('dynamicTextbox');
    dynamicTextbox.style.display = 'block';
    dynamicTextbox.classList.add('fade-in');

    // Add smooth scrolling to navigation links
    document.querySelectorAll('a[href^="#"]').forEach((e) => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
};

// Function to check if an element is in the viewport
function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Fade in the iframe when it is in the viewport
window.addEventListener('scroll', function() {
    var iframe = document.querySelector('.pdf-container iframe');
    if (isInViewport(iframe)) {
        iframe.classList.add('fade-in');
    }
});

// Function to check if an element is in the viewport
function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Fade in team member photos one after the other
window.addEventListener('scroll', function() {
    var teamMembers = document.querySelectorAll('.team-member img');
    teamMembers.forEach(function(member, index) {
        if (isInViewport(member) && !member.classList.contains('fade-in')) {
            setTimeout(function() {
                member.classList.add('fade-in');
            }, index * 500); // Adjust the delay (500ms in this example) between each photo
        }
    });
});


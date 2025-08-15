/* Add this JavaScript to create particles */
function createParticles() {
    const particles = 50;
    for (let i = 0; i < particles; i++) {
      const particle = document.createElement('div');
      particle.classList.add('particle');
      
      // Random size between 2px and 5px
      const size = Math.random() * 3 + 2;
      particle.style.width = `${size}px`;
      particle.style.height = `${size}px`;
      
      // Random position
      particle.style.left = `${Math.random() * 100}vw`;
      particle.style.top = `${Math.random() * 100}vh`;
      
      // Random animation duration between 10s and 30s
      const duration = Math.random() * 20 + 10;
      particle.style.animationDuration = `${duration}s`;
      
      // Random delay
      particle.style.animationDelay = `${Math.random() * 5}s`;
      
      document.body.appendChild(particle);
    }
  }

  
// Call this function when the page loads
window.onload = createParticles;
  
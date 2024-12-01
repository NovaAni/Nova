// Initial countdown value
let countdown = 5;
        
// Function to update the countdown
function updateTimer() {
  // Update the text with "Starting in" followed by the countdown number
  document.getElementById('countdownText').textContent = "Starting in " + countdown;

  // Decrease the countdown value
  countdown--;
  let condition =  (document.getElementById());

  // When countdown reaches 0, stop the timer and redirect to html.html
  if (countdown < 0 ) {
    clearInterval(timerInterval); // Stop the interval
    window.location.href = "python.html"; // Redirect to html.html
  }
}

// Start the countdown timer, update every 1000ms (1 second)
let timerInterval = setInterval(updateTimer, 1000);

// Ensure it starts immediately without waiting for the first interval
updateTimer();
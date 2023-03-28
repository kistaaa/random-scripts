var context = new AudioContext();
var oscillator = context.createOscillator();
var gainNode = context.createGain();

oscillator.connect(gainNode);
gainNode.connect(context.destination)

oscillator.start();

stopButton.addEventListener('click', function() {
    // Important! Setting a scheduled parameter value
    gainNode.gain.setValueAtTime(gainNode.gain.value, context.currentTime); 

    gainNode.gain.exponentialRampToValueAtTime(0.0001, context.currentTime + 0.03);
});

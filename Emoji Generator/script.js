async function generateEmoji() {
    try 
    {
        const response = await fetch('https://api.emojisworld.fr/v1/random');
        const data = await response.json();
        const emoji = data.results[0].emoji;
        const name = data.results[0].name;

        document.getElementById('emoji-symbol').textContent = emoji;
        document.getElementById('emoji-name').textContent = name;
    } 
    catch (error) {
        console.error('Error fetching emoji:', error);
        document.getElementById('emoji-symbol').textContent = '❌';
        document.getElementById('emoji-name').textContent = 'Error loading emoji';
    }
}

document.getElementById('generate-emoji').addEventListener('click', generateEmoji);
document.addEventListener('DOMContentLoaded', () => {
    generateEmoji(); // Generate an emoji on page load
});


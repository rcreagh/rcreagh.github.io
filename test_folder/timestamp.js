// Function to display data from txt file in webpage.

var xhr = new XMLHttpRequest;
xhr.open('GET', 'timestamp.txt', true);
xhr.onload = function (){
    document.write(xhr.responseText);
};
xhr.send(null);

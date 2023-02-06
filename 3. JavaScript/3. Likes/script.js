var CountLikes = 1
var CountLikesElement = document.querySelector("#CountLikes")
function add1() {
    CountLikes++;
    CountLikesElement.innerText = CountLikes + " like(s)"
    console.log(CountLikes)
}


var CountLikes2 = 1
var CountLikes2Element = document.querySelector("#CountLikes2")
function add2() {
    CountLikes2++;
    CountLikes2Element.innerText = CountLikes2 + " like(s)"
    console.log(CountLikes2)
}

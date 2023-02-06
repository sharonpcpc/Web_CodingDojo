var profilename = document.querySelector ("#profilename");

function clickeditprofile() {
    profilename.innerText = "Sharon Pineda";
}


var connectionsrequests1 = document.querySelector ("#connectionsrequests");

function AcceptInvitation (id) {
    var element = document.querySelector(id)
    element.remove();
    connectionsrequests1.innerText--;

}

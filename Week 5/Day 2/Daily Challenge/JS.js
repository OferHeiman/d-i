let button = document.getElementById('lib-button');
button.addEventListener("click", tellStory);
function tellStory() {
    let input1Text = document.getElementById('noun').value;
    let input2Text = document.getElementById('adjective').value;
    let input3Text = document.getElementById('person').value;
    let input4Text = document.getElementById('verb').value;
    let input5Text = document.getElementById('place').value;
    let paragraph = document.getElementById('story');
    if (input1Text.length == 0 || input2Text.length == 0 || input3Text.length == 0 || input4Text.length == 0 || input5Text.length == 0) {
        alert("Please make sure all fields are filled");
        return;
    }
    else {
        let story = "An " + input1Text + " by the name of " + input3Text + "," + input4Text + " on planet " + input5Text + ",a " + input2Text + " landscape.";
        //example noun=astronaut,adjective=hellish,person=Selene,verb=crashed,place=Atropos
        paragraph.innerText = story;
    }
}

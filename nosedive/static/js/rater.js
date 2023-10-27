export function Rater(ratingElement) {
    const stars = ratingElement.querySelectorAll(".star");


    for (let i = 0; i < stars.length; i++) {
        const star = stars[i];


        star.addEventListener("mouseenter", function (event) {

            for (let j = 0; j <= i; j++) {
                stars[j].classList.toggle("selecting")
            }

            //console.log(event.type)
            //console.log("star" + String(i))

        });
        star.addEventListener("mouseleave", function (event) {

            for (let j = 0; j < stars.length; j++) {
                stars[j].classList.remove("selecting")
            }
        });


        star.addEventListener("click", function (event) {
            var input_stars = stars[i].parentNode.querySelectorAll('input[id=id_stars]')[0];
            input_stars.value = i+1;


            var input_user = stars[i].parentNode.querySelectorAll('input[id=id_rated_user]')[0];
            var rated_user = stars[i].parentNode.getAttribute("rated_user");
            input_user.value = rated_user;

            

            var form = stars[i].parentNode.getElementsByTagName("form")[0];

            form.submit();
            


            
            console.log(rated_user);
            console.log("click"+stars[i].parentNode.getAttribute("data-value")+stars[i].getAttribute("data-value"));
        });
    }

    
    

    

}

import {Rater} from './rater.js'

document.addEventListener('DOMContentLoaded', function(){
    const raters = document.querySelectorAll("[role=rater]");
    raters.forEach(rater => {
        new Rater(rater);
    })

})


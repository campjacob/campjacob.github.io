---
---
/* ==========================================================================
   Custom JS
   ========================================================================== */

var myArray = [
	{% for term in site.dictionary %}
	"{{ term.title }}"{% unless forloop.last %},{% endunless %}
	{% endfor %}
];
var randomItem = myArray[Math.floor(Math.random()*myArray.length)];
//document.body.innerHTML = randomItem;
document.getElementById("RandomWord").innerHTML = "<a href='/dictionary/" + randomItem + "' class='btn btn--inverse btn--small'>" + randomItem + "</a>";

// Instructions

// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.
// Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).
// Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result. 
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.





let sentance = prompt("Enter a sentance");
wordNot = sentance.indexOf("not");
console.log(wordNot)
wordBad = sentance.indexOf("bad");
console.log(wordBad)

console.log(sentance.slice(wordBad+3, ));
if (wordNot===-1) {alert(sentance);
}
else if (wordNot < wordBad) {alert(sentance.slice(0,wordNot) + " good" + sentance.slice(wordBad+3, ));
}
else if (wordNot > wordBad) {alert(sentance);
}
else {alert(sentance);}
const prompt = require("prompt");
const { serialize } = require("v8");
prompt.start();

console.log("© Boricraft-Development 2021\nhttps://github.com/Boricraft-Developmont")
console.log("Wow such development");
prompt.get('amount', function (err, result) {
    console.log(result.amount)
    var mcolor = null
    var msize = null
    var i = 0

    while (result.amount > i) {
        console.log(i);
        i++;
    
    
    var rng1 = Math.floor(Math.random() * 3);
    switch (rng1) {
        case 0:
            mcolor = "black"
        break;
        case 1:
            mcolor = "brown"
        break;
        case 2:
            mcolor = "white"
        break;
        }
    
    var rng2 = Math.floor(Math.random() * 4);
    switch (rng2) {
        case 0:
            msize = "big"
        break;
        case 1:
            msize = "medium"
        break;
        case 2:
            msize = "small"
        break;
        case 3:
            msize = "tiny"
        break;
    }
    console.log('The monke is ' + msize + ' and has ' + mcolor + ' fur.')
    }
})





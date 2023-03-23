#!/usr/bin/node
/**
 * class square inherits from square
 */
const Squarei = require('./5-square');

module.exports = class Square extends Squarei {
    charPrint(c){
        if (c === undefined){
            this.print();
        }
        else{
            for (let i = 0; i < this.height; i++){
                let string = '';
                for (let j = 0; j <this.width; j++){
                    string += c;
                }
                console.log(string);
            }  
        }
    }
}

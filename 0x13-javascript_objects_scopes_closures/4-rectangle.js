#!/usr/bin/node
/*
Write a class Rectangle
*/
module.exports = class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        }
    }

    print () {
        for (let n = 0; n < this.height; n++){
            console.log('X'.repeat(this.width));
        }
    }

    rotate () {
        let w2 = this.height;
        let h2 = this.width;
        this.width = w2;
        this.height = h2;
    }

    double() {
        this.width = this.width * 2;
        this.height = this.height * 2;
    }
};  
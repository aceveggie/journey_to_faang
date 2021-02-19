class DynamicArray {
    constructor()
    {
        this.capacity = 1;
        this.length = 0;
        this.theArray = this.makeArray(1)
    }

    makeArray(capacity)
    {
        // User .filter() method to create array with fixed array size
        // If the return value is true, 
            // the element is included in the returned array, 
            // otherwise it is ignored.)
        return Array(capacity).filter(function(value){
            return value == 2
        });
    }

    addElement(ele)
    {
        if(this.capacity === this.theArray.length)
        {
            console.log("arrayLenght: "+this.theArray.length+", arrayCapacity: "+this.capacity)
            console.log("increasing array size to: "+this.capacity *2)
            this.increaseSize().then(()=>{
                this.theArray.push(ele)
                console.log(this.theArray)
            })
        }
        else
        {
            this.theArray.push(ele)
            console.log(this.theArray)
        }
    }

    async increaseSize()
    {
        this.newArray = this.makeArray(this.capacity*2);

        for(var i=0; i<this.theArray.length; i++)
        {
            this.newArray[i] = this.theArray[i];
        }
        this.capacity = this.capacity*2;
        this.theArray = this.newArray.slice()
    }
}

var addEleToDynArray = new DynamicArray();
addEleToDynArray.addElement(1)
addEleToDynArray.addElement(2)
addEleToDynArray.addElement(3)
addEleToDynArray.addElement(4)
addEleToDynArray.addElement(5)
addEleToDynArray.addElement(6)
addEleToDynArray.addElement(7)
addEleToDynArray.addElement(8)
addEleToDynArray.addElement(9)
addEleToDynArray.addElement(10)
// Allocate a new array B with larger capacity (A commonly used rule for the new array is to have twice the capacity of the existing array )
// Set B[i]=A[i], for i=0 to n-1 where n denotes the current no of items.
// Set A=B that is, we hence forth use B as the array of supporting list.
// Insert new element in the new array.
var DynamicArray = /** @class */ (function () {
    function DynamicArray(ele) {
        this.numOfEle = 0;
        this.capacity = 1;
        this.numOfEle = 0;
        this.capacity = 1;
        this.theArray = this.makeArray(this.capacity);
    }
    DynamicArray.prototype.addElement = function (element) {
        if (this.numOfEle === this.capacity) {
            this.increaseSize(this.capacity);
        }
        else {
            this.theArray.push(element);
            console.log(this.theArray);
        }
    };
    DynamicArray.prototype.makeArray = function (capacity) {
        if (capacity === void 0) { capacity = null; }
        return Array(capacity);
    };
    DynamicArray.prototype.increaseSize = function (capacity) {
        this.capacity = capacity * 2;
        this.newArray = this.makeArray(this.capacity);
        for (var i = 0; i < this.theArray.length; i++) {
            this.newArray[i] = this.theArray[i];
        }
        this.theArray = this.newArray;
    };
    return DynamicArray;
}());
var addEleToDynArray = new DynamicArray(1);
addEleToDynArray.addElement(1);
addEleToDynArray.addElement(3);
addEleToDynArray.addElement(2);
addEleToDynArray.addElement(2);
addEleToDynArray.addElement(2);
addEleToDynArray.addElement(5);
addEleToDynArray.addElement(5);
addEleToDynArray.addElement(5);
addEleToDynArray.addElement(4);
addEleToDynArray.addElement(4);
addEleToDynArray.addElement(2);

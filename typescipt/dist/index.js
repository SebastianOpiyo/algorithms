"use strict";
// watch file with <--watch>
// compile with <tsc>
// Basic Types
let id = 5;
let company = 'It-Sealops';
let isPublished = true;
let x;
// Advanced Datatypes
//1. arrays
let myNumList;
let arrayForAll;
//2. tuples
let myTuple;
// array of tuples
let complexTuple;
// Union
let union;
// Enum
var CompassPoints;
(function (CompassPoints) {
    CompassPoints[CompassPoints["North"] = 0] = "North";
    CompassPoints[CompassPoints["South"] = 1] = "South";
    CompassPoints[CompassPoints["East"] = 2] = "East";
    CompassPoints[CompassPoints["West"] = 3] = "West";
})(CompassPoints || (CompassPoints = {}));
var CompassPoints2;
(function (CompassPoints2) {
    CompassPoints2["North"] = "North";
    CompassPoints2["South"] = "South";
    CompassPoints2["East"] = "East";
    CompassPoints2["West"] = "West";
})(CompassPoints2 || (CompassPoints2 = {}));
// Type ascertion
let myId = 100;
let customerId = myId;
// Alternatively.
let stringId = myId;
// Functions
// function with return
function addNum(x, y) {
    return x + y;
}
// function without return i.e void function
function logMessage(message) {
    console.log(message);
}
const add = (x, y) => x + y;
const sub = (x, y) => x - y;
// classes
class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }
}
class EmployeeDetails {
    constructor(name, id, location) {
        this.name = name;
        this.id = id;
        this.location = location;
    }
}
const employee = new EmployeeDetails("Sebastian Opiyo", 34, "nairobi");
// TESTS
x = "My name is sebastian";
// x = 4
// x
console.log(x);
// myNumList
myNumList = [1, 45, 98, 100];
arrayForAll = ['Sebastian', 31, 'Male', [12, 46, 90]];
// myTuple
myTuple = ['Alex', 45];
// complex tuple
complexTuple = [
    [1, 'Sebastian'],
    [2, 'Alex'],
    [3, 'Martin'],
    [4, 'Consolata']
];
// Union
// union = 'Shabaz'
union = 190;
// Object
const user = {
    id: 1,
    name: "Joseph"
};
// Type ascertions
stringId = '200';
// classes
const Peter = new Person(1, "Peter Johnson");
const John = new Person(2, "John Doe");
// Test Out
// console.log(myNumList)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(arrayForAll)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(myTuple)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(complexTuple)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(union)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(CompassPoints.North)
// console.log(CompassPoints.East)
// console.log(CompassPoints.West)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(CompassPoints2.North)
// console.log(CompassPoints2.East)
// console.log(CompassPoints2.West)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(user)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(customerId)
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(stringId)
// console.log('-.-.-.-.-.-.-.-.-')
// addNum(4,62)
// logMessage("I am Home!")
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(add(8, 90))
// console.log(sub(89, 70))
// console.log('-.-.-.-.-.-.-.-.-')
// console.log(Peter.name)
// console.log(John.id)
console.log('-.-.-.-.-.-.-.-.-');
// console.log(employee);
console.log(employee.name, employee.location);

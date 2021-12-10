// watch file with <--watch>
// compile with <tsc>


// Basic Types

let id: number = 5
let company: string = 'It-Sealops'
let isPublished: boolean = true
let x: any 

// Advanced Datatypes

//1. arrays
let myNumList: number[] 
let arrayForAll: any []

//2. tuples
let myTuple: [string, number]
// array of tuples
let complexTuple: [number, string] []

// Union
let union: string | number

// Enum
enum CompassPoints {
    North, 
    South,
    East,
    West
}

enum CompassPoints2 {
    North = "North", 
    South = "South",
    East = "East",
    West = "West"
}

// Objects
type User = {
    id: number,
    name: string
}

// Type ascertion
let myId: any = 100 
let customerId = <number> myId
// Alternatively.
let stringId = myId as string 


// Functions

// function with return
function addNum(x:number, y:number){
    return x + y 
}

// function without return i.e void function
function logMessage(message: string | number):void {
    console.log(message)
}

// Interfaces
interface mathFunc {
    (x:number, y:number): number 
}

const add:mathFunc = (x:number, y:number): number => x + y 
const sub:mathFunc = (x:number, y:number): number => x - y 

// classes
class Person {
    // we can have the attributes as
    /*
    - private
    - protected
    - Or public 
    */


    id: number
    name: string

    constructor(id:number, name:string){
        this.id = id
        this.name = name

    }
}


interface Employee {
    name: string;
    id: number;
    location: string;
}

class EmployeeDetails {
    name: string;
    id: number;
    location: string;

    constructor(name:string, id: number, location:string){
        this.name = name;
        this.id = id;
        this.location = location;
    }
}

const employee: Employee = new EmployeeDetails("Sebastian Opiyo", 34, "nairobi");


// TESTS
x = "My name is sebastian"
// x = 4

// x
console.log(x)

// myNumList
myNumList = [ 1, 45, 98, 100]
arrayForAll = ['Sebastian', 31, 'Male', [12, 46, 90]]

// myTuple
myTuple = ['Alex', 45]

// complex tuple
complexTuple = [
    [1, 'Sebastian'],
    [2, 'Alex'],
    [3, 'Martin'],
    [4, 'Consolata']
]

// Union
// union = 'Shabaz'
union = 190


// Object
const user: User = {
    id: 1,
    name : "Joseph"
}

// Type ascertions
stringId = '200'

// classes
const Peter = new Person(1, "Peter Johnson")
const John = new Person(2, "John Doe")

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

console.log('-.-.-.-.-.-.-.-.-')
// console.log(employee);
console.log(employee.name, employee.location);
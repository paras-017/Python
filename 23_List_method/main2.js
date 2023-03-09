let arr = [1,2,3,4,5]
let arr2 = arr
arr2[0] = 0
console.log(arr)
console.log(arr2)

// Here arr2 is the reference of arr1 .In the memory array is same now if you write arr2 = arr and then if  you change  arr2 so arr will also be  changed because you made arr2 as a  reference of arr
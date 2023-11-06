// this === global = true

/*
console.log()
console.error()
// Codigo después de un intervalo de tiempo
setTimeout(() => {})
// Codigo cada intervalo de timepo
setInterval(() => {})
// Da prioridad de ejecución a una Fn async
setImmediate(() => {})
*/

// console.log(setInterval);

let i = 0
let intervalo = setInterval(() => {
    console.log('Hola')
    if (i === 3) {
        clearInterval(intervalo)
    }
    i++
}, 1000)

setImmediate(() => {
    console.log('Saludo inmediato')
})


// require()

console.log(__filename)

global.miVariable = 'Mi variabble global'

console.log(miVariable);
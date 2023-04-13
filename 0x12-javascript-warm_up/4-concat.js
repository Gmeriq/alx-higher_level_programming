#!usre/bin/node

//Prints arguments in a format

if (process.argv[1] === null)
{
    console.log("undefine is undefined");
}
else if (process.argv[2] === null)
{
    console.log("${process.argv[1]} is undefined");
}
else
{
    console.log("${process.argv[1]} is ${process.argv[2]}");
}

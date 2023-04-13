#!/usr/bin/node

//Prints arguments in a format


if (process.argv[2] === null)
{
    console.log("undefine is undefined");
}
else if (process.argv[3] === null)
{
    console.log("${process.argv[2]} is undefined");
}
else
{
    console.log("${process.argv[3]} is ${process.argv[2]}");
}

#!/usr/bin/node

// Print first argument

const argv = process.argv;
if (argv[1] === null)
{
    console.log("No argument");
}
else
{
    console.log(argv[1]);
}

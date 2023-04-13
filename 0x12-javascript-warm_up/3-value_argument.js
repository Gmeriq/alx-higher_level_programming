#!/usr/bin/node

// Print first argument

const argv = process.argv;
if (argv === null)
{
    console.log("No argument");
}
else
{
    console.log(argv[0]);
}

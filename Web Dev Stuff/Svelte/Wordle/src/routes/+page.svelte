<script lang='ts'>
    let guesses = ['','','','','',''];
    let currentGuess = 1;
    let currentLetter = 1;

    $: console.log(guesses);

</script>

<svelte:head>
    <title>Wordle by K7</title>
    <meta name="description" content="Wordle by K7">
    <meta name="keywords" content="Wordle, K7">
    <meta name="author" content="K7">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</svelte:head>


<div class="bg-black flex justify-center font-medium w-screen h-screen text-white">
    <h1 class="text-xl mt-32 h-10">Wordle by K7</h1>
    <div class="bg-blue-500 w-1/4 h-1/2 text-center justify-center absolute top-48 rounded-lg">
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
            <div class="border relative w-full mt-4 h-16 items-center justify-center flex">
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
                <div class="p-2 text-lg border-black border-2 w-16 h-10 flex justify-center items-center mr-1"></div>
            </div>
        </div>
</div>


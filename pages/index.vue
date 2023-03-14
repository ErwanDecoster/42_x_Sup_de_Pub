<template>
  <div>
    <section class="background w-full h-[95vh] flex justify-center items-center">
      <img
        class="h-[43rem] absolute -right-0 -top-32"
        src="@/src/halfcirclegreen+dot.svg"
        alt=""
      >
      <img
        class="h-[60rem] absolute -top-80 -left-8 opacity-20"
        src="@/src/whitesnake.svg"
        alt=""
      >
      <img
        class="h-[30rem] bottom-14 left-0 absolute"
        src="@/src/logo_square.svg"
        alt=""
      >
      <div class="z-10">
        <div class="custom-shadow h-0 w-0 rounded-full bg-maastricht-blue absolute top-1/2 left-1/2 -z-10" />
        <h1 class="text-white text-8xl relative -translate-y-1/2">
          ÉDITION
          <span class="text-khaki text-10xl font-bold absolute left-1/2 -translate-x-1/2 top-14">2023</span>
        </h1>
        <div class="flex flex-col items-center gap-8 mt-20">
          <p class="text-white">
            Du <b>31.05</b> au <b>28.07</b>
          </p>
          <div class="flex gap-5">
            <NuxtLink
              to=""
              class="button-secondary"
            >
              Programmation
            </NuxtLink>
            <NuxtLink
              to=""
              class="button-primary-two"
            >
              Billeterie
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
    <section class="bg-maastricht-blue w-full h-[80vh] relative">
      <div class="mx-auto max-w-screen-xl">
        <div>
          // caoucel
        </div>
        <div>
          <h2 class="text-white text-5xl static left-3/4 top-1/2">
            UN INIMITABLE
            <span class="text-khaki text-7xl relative -left-1 -top-4 font-bold">FESTIVAL</span>
          </h2>
          <p></p>
          <NuxtLink class=""></NuxtLink>
        </div>
      </div>

    </section>
  </div>
</template>
<style>
  .background
  {
    background-image: url('@/src/background.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }
  .custom-shadow
  {
    box-shadow: 0px 0px 250px 250px rgba(1,22,39,1);

  }
</style>

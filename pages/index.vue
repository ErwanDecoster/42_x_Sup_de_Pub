<template>
  <div>
    <section class="background w-full h-[95vh] flex justify-center items-center">
      <img
        class="h-[40rem] -top-44 -right-0 absolute  z-0"
        src="../public/halfcirclegreen+dot.svg"
        alt=""
      >
      <img
        class="absolute -top-64 left-14 z-0 h-[50rem] opacity-20"
        src="../public/whitesnake.svg"
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
  </div>
</template>
<style>
  .background
  {
    background-image: url('@/public/background.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }
  .custom-shadow
  {
    box-shadow: 0px 0px 250px 250px rgba(1,22,39,1);

  }
</style>

<template>
  <div>
    <section class="background w-full h-[100vh] flex justify-center items-center">
      <img
        class="absolute h-0 top-[6.75rem] right-[0.75rem] md:h-[43rem] md:-right-0 md:-top-32"
        src="@/src/halfcirclegreen+dot.svg"
        alt=""
      >
      <img
        class="md:h-[60rem] absolute -top-80 -left-36 opacity-20"
        src="@/src/whitesnake.svg"
        alt=""
      >
      <img
        class="h-44 -bottom-16 md:h-[50rem] absolute md:-bottom-[19rem] left-0"
        src="@/src/demi-cercle-jaune-logo.svg"
        alt=""
      >
      <div class="z-10">
        <div class="custom-shadow h-0 w-0 rounded-full bg-maastricht-blue absolute top-1/2 left-1/2 -z-10" />
        <h1 class="text-white text-5xl md:text-8xl flex flex-col items-center">
          ÉDITION
          <span class="text-khaki text-7xl font-bold relative -top-6 md:text-10xl md:-top-11">2023</span>
        </h1>
        <div class="flex flex-col items-center gap-6 md:-mt-6 md:text-2xl">
          <p class="text-white">
            Du <b>31.05</b> au <b>28.07</b>
          </p>
          <div class="flex gap-5">
            <NuxtLink
              to=""
              class="button-primary-two"
            >
              PROGRAMMATION & BILLETERIE
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
    <section class="bg-maastricht-blue w-full h-[80vh] md:flex md:justify-center md:items-center">
      <div class="max-w-screen-xl flex-col md:grid md:grid-cols-5 md:gap-52">
        <div class="order-7 md:order-first md:col-span-3">
          <Carrousel />
        </div>
        <div class="order-2 md:col-span-2">
          <h2 class="text-white text-5xl ">
            UN INIMITABLE
            <span class="text-khaki text-7xl relative -top-5 -left-1 font-bold">FESTIVAL</span>
          </h2>
          <p class="text-white mt-5 mb-5">
            Les Nuits de Fourvière sont un <b>festival culturel pluridisciplinaire</b> (théâtre, musique, danse, cinéma...)
            se déroulant chaque été (en juin, juillet et août) depuis 1946 au Théâtre antique de Fourvière
            (de 2 600 à 4 500 places), dans le 5e arrondissement de Lyon, près de la basilique du même nom.
          </p>
          <NuxtLink class="button-primary relative -left-1">
            QUI SOMMES NOUS ?
          </NuxtLink>
        </div>
      </div>
      <div>
        <img
          class="absolute rotate-180 right-[6rem] -bottom-[67em]"
          src="@/src/outline_circle.svg"
          alt=""
        >
      </div>
      <img
        class="absolute w-32 rotate-180 right-[2rem] -bottom-[58em] opacity-95"
        src="@/src/circle.svg"
        alt=""
      >
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

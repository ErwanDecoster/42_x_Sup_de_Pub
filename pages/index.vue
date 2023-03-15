<template>
  <div>
    <section class="background w-full h-[100vh] flex justify-center items-center">
      <img
        class="h-[43rem] absolute -right-0 -top-32"
        src="@/src/halfcirclegreen+dot.svg"
        alt=""
      >
      <img
        class="h-[60rem] absolute -top-80 -left-36 opacity-20"
        src="@/src/whitesnake.svg"
        alt=""
      >
      <img
        class="h-[50rem] -bottom-[19rem] left-0 absolute"
        src="@/src/demi-cercle-jaune-logo.svg"
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
    <section class="bg-maastricht-blue w-full h-[80vh] flex justify-center items-center">
      <div class="max-w-screen-xl grid grid-cols-5 gap-52">
        <div class="col-span-3">
          <carrousel />
        </div>
        <div class="col-span-2">
          <h2 class="text-white text-5xl ">
            UN INIMITABLE
            <span class="text-khaki text-7xl relative -top-5 -left-1 font-bold">FESTIVAL</span>
          </h2>
          <p class="text-white mt-5 mb-5">
            Les Nuits de Fourvière sont un <bold>festival culturel pluridisciplinaire</bold> (théâtre, musique, danse, cinéma...)
            se déroulant chaque été (en juin, juillet et août) depuis 1946 au Théâtre antique de Fourvière
            (de 2 600 à 4 500 places), dans le 5e arrondissement de Lyon, près de la basilique du même nom.
          </p>
          <NuxtLink class="button-primary relative -left-1">
            QUI SOMMES NOUS ?
          </NuxtLink>
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

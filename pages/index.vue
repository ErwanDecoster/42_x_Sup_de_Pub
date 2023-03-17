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
    <section class="bg-maastricht-blue w-full p-8 md:h-[80vh] md:flex md:justify-center md:items-center">
      <div class="max-w-screen-xl grid gap-16 md:grid-cols-5 md:gap-52">
        <div class="order-last mb-16 md:order-first md:col-span-3">
          <Carrousel />
        </div>
        <div class="z-50order-first mt-3 md:col-span-2">
          <h2 class="text-white text-3xl mb-4 md:text-5xl ">
            UN INIMITABLE
            <span class="text-khaki text-5xl md:text-7xl relative -top-4 md:-top-6 -left-1 font-bold">FESTIVAL</span>
          </h2>
          <p class="text-white md:mt-5 mb-5">
            Les Nuits de Fourvière sont un <b>festival culturel pluridisciplinaire</b> (théâtre, musique, danse, cinéma...)
            se déroulant <b>chaque été</b> (en juin, juillet et août) <b>depuis 1946</b> au <b>Théâtre antique de Fourvière</b>
            (de 2 600 à 4 500 places), dans le <b>5e arrondissement de Lyon</b>, près de la basilique du même nom.
          </p>
          <NuxtLink class="button-primary-two md:button-primary relative -left-1">
            QUI SOMMES NOUS ?
          </NuxtLink>
        </div>
      </div>
      <div>
        <img
          class="h-0 absolute md:rotate-180 md:right-[6rem] md:-bottom-[67em]"
          src="@/src/outline_circle.svg"
          alt=""
        >
      </div>
      <img
        class="h-0 absolute md:w-32 md:rotate-180 md:right-[2rem] md:-bottom-[58em] opacity-95"
        src="@/src/circle.svg"
        alt=""
      >
    </section>
    <section class="bg-[#1a2d3d] w-full p-5 md:p-[8.25rem] md:flex md:flex-col md:justify-center md:items-center">
      <div class="md:grid md:grid-cols-3 md:gap-4 md:items-center md:justify-center md:mx-8">
        <h2 class="text-white text-3xl mb-4 md:text-5xl md:mb-auto">
          DE NOMBREUX
          <span class="text-khaki text-5xl relative -left-1 font-bold -top-4 md:text-7xl md:-top-6">ARTISTES</span>
        </h2>
        <p class="text-white mb-5 md:w-2/3">
          Depuis plus de 75 ans, le festival produit et crée des spectacles originaux et audacieux...
        </p>
        <NuxtLink class="md:justify-self-end md:button-primary button-primary-two">
          TOUTE LA PROGRAMMATION
        </NuxtLink>
      </div>
      <div class="py-10 flex flex-row gap-6 overflow-x-auto overflow-y-auto snap-mandatory snap-x md:w-full md:grid md:grid-cols-4 md:gap-0">
        <div class="snap-center my-6 ">
          <Artist
            name="FLORENCE FORESTI"
            img="florence_foresti.jpeg"
            theme="HUMOUR"
            days="25-30"
            month="06"
            fontSize="22"
            description="Elle revient avec son nouveau seule-en-scène intitulé Boys..."
          />
        </div>
        <div class="snap-center my-6">
          <Artist
            name="MICHEL POLNAREFF"
            img="michel_polnareff.jpeg"
            theme="MUSIQUE"
            days="16"
            month="06"
            fontSize="22"
            description="Sa voix, intacte, et son sensationnel jeu de piano, font tout..."
          />
        </div>
        <div class="snap-center my-6">
          <Artist
            name="BENJAMIN BIOLAY"
            img="benjamin_biolay.jpeg"
            theme="MUSIQUE"
            days="05-06"
            month="07"
            fontSize="22"
            description="“Je voulais vous le dire avant qu’on enchaîne, c’est toujours une émotion folle d’être ici…”"
          />
        </div>
        <div class="snap-center my-6">
          <Artist
            name="ZAZIE"
            img="zazie.jpeg"
            theme="HUMOUR"
            days="12"
            month="07"
            fontSize="22"
            description="Elle affiche fièrement ses tempes grisonnantes, libérée de ne plus les masquer..."
          />
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

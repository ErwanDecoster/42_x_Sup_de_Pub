<template>
  <div class="flex flex-col w-full z-10">
    <div class="flex bg-maximum-blue-green w-full">
      <div class="flex lg:items-center flex-col m-auto lg:flex-row justify-between gap-10 max-w-screen-2xl w-full py-12 px-6">
        <div>
          <p class="whitespace-nowrap w-auto text-5xl">
            RÉSERVEZ VOS
          </p>
          <p class="-mt-6 -ml-1 text-7xl font-bold">
            BILLETS
          </p>
        </div>
        <p class="text-base max-w-sm font-normal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt...
        </p>
        <NuxtLink
          to=""
          class="button-bg-secondary"
        >
          ACCÉDER À LA BILLETTERIE
        </NuxtLink>
      </div>
    </div>
    <div class="relative flex bg-black w-full pb-52">
      <div class="grid m-auto md:grid-cols-2 grid-cols-1 xl:grid-cols-4 justify-between gap-8 max-w-screen-2xl w-full py-12 px-6">
        <div class="flex flex-col md:order-1 order-3 h-40 justify-between">
          <p class="whitespace-nowrap text-white font-bold text-2xl">
            LES NUITS DE FOURVIÈRE
          </p>
          <p class="text-white text-base">
            1 rue Cléberg<br>69005 Lyon
          </p>
          <p class="whitespace-nowrap text-white ext-base font-bold">
            INFORMATIONS : 04 72 57 15 40<br>BILLETTERIE : 04 72 32 00 00
          </p>
        </div>
        <div class="flex flex-col md:order-2 order-2">
          <p class="whitespace-nowrap text-white font-bold text-2xl mb-5">
            RÉSEAUX SOCIAUX
          </p>
          <div class="flex gap-6">
            <NuxtLink
              to=""
              class="border-4 border-khaki rounded-full px-2 py-2 cursor-pointer"
            >
              <img
                class="h-5 w-6 min-w-[24px] min-h-[20px]"
                src="@/src/icone_facebook.svg"
                alt=""
              >
            </NuxtLink>
            <NuxtLink
              to=""
              class="border-4 border-khaki rounded-full px-2 py-2 cursor-pointer"
            >
              <img
                class="h-5 w-6 min-w-[24px] min-h-[20px]"
                src="@/src/icone_twitter.svg"
                alt=""
              >
            </NuxtLink>
            <NuxtLink
              to=""
              class="border-4 border-khaki rounded-full px-2 py-2 cursor-pointer"
            >
              <img
                class="h-5 w-6 min-w-[24px] min-h-[20px]"
                src="@/src/icone_instagram.svg"
                alt=""
              >
            </NuxtLink>
            <NuxtLink
              to=""
              class="border-4 border-khaki rounded-full px-2 py-2 cursor-pointer"
            >
              <img
                class="h-5 w-6 min-w-[24px] min-h-[20px]"
                src="@/src/icone_youtube.svg"
                alt=""
              >
            </NuxtLink>
          </div>
        </div>
        <div class="flex flex-col md:order-3 order-4">
          <p class="whitespace-nowrap text-white font-bold text-2xl mb-5">
            PLAN DU SITE
          </p>
          <NuxtLink
            to="/"
            class="button-simple text-base font-bold normal-case p-0"
          >
            Accueil
          </NuxtLink>
          <NuxtLink
            to="/about_us"
            class="button-simple text-base font-bold normal-case p-0"
          >
            Qui sommes-nous ?
          </NuxtLink>
          <NuxtLink
            to=""
            class="button-simple text-base font-bold normal-case p-0"
          >
            Infos pratiques
          </NuxtLink>
          <NuxtLink
            to="/infos"
            class="button-simple text-base font-bold normal-case p-0"
          >
            Programmation
          </NuxtLink>
          <NuxtLink
            to="/programming_and_ticketing"
            class="button-simple text-base font-bold normal-case p-0"
          >
            Billetterie
          </NuxtLink>
        </div>
        <div class="flex flex-col md:order-4 order-1 gap-5">
          <p class="text-white font-bold text-2xl">
            NEWSLETTER
          </p>
          <p class="text-white text-base max-w-xs">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </p>
          <div>
            <p class="text-white text-base pb-2">
              Adresse email
            </p>
            <div class="flex flex-row">
              <input 
                type="text" 
                class="px-5 py-2 pr-7 text-white bg-black border-2 border-white rounded-l-full outline-none" 
              >
              <p class="button-primary -ml-5 hover:bg-black">
                S'ABONNER
              </p>
            </div>
          </div>
        </div>
      </div>
      <img
        class="absolute h-64 bottom-0 left-0"
        src="@/src/logo_square.svg"
        alt=""
      >
      <img
        class="absolute w-40 h-16 sm:w-72 sm:h-28 md:bottom-36 sm:bottom-28 md:left-96 sm:left-60 left-56 bottom-20"
        src="@/src/logo_metropole.png"
        alt=""
      >
    </div>
    <div class="flex bg-alizarin-crimson w-[3000px]">
      <p class="absolute text-white p-2 left-80">
        CE & Collectivités - Mentions légales - Presse - Règlement du festival & CGV - Technique - 
        Politique de confidentialité - Cookies
      </p>
    </div>
  </div>
</template>
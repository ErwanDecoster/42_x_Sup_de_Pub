<template>
  <div class="fixed z-20 h-32 w-full flex">
    <div class="flex justify-between max-w-screen-xl m-auto w-full">
      <img
        class="h-16"
        src="@/public/logo.svg"
        alt=""
      >
      <div class="flex gap-12 items-center ">
        <NuxtLink
          to=""
          class="button-simple "
        >
          QUI SOMMES NOUS?
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-simple "
        >
          INFOS PRATIQUES
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-simple "
        >
          PROGRAMMATION
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary"
        >
          BILLETERIE
        </NuxtLink>
        <NuxtLink
          to=""
          class="button-primary-two px-2"
        >
          <img
            class="h-5 w-6"
            src="@/public/icone_panier_noir.svg"
            alt=""
          >
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
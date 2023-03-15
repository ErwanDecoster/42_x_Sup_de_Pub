<template>
  <div class="pt-36 pb-12 lg:pb-24 space-y-12 lg:space-y-24 px-6">
    <div class="mx-auto w-fit space-y-7">
      <h1 class="uppercase text-8xl text-khaki">
        Panier
      </h1>
      <p class="text-white w-fit mx-auto">
        <NuxtLink
          to="/"
          class="font-bold underline"
        >
          Acceuil
        </Nuxtlink> > Panier
      </p>
    </div>
    <OrderForm />
  </div>
</template>
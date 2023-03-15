<template>
  <div class="max-w-screen-2xl mx-auto bg-white">
    <div class="h-36 px-2 md:px-4 lg:px-16 xl:px-32 grid grid-cols-4 border-b-4 border-platinum">
      <div 
        class="font-bold text-center border-b-4 -mb-1 relative flex flex-col justify-center gap-2"
        :class="`${ state == 1 ? 'border-black' : 'border-platinum'}`"
      >
        <p class="text-4xl">
          1
        </p>
        <p class="text-xxs lg:text-xl uppercase">
          Panier
        </p>
        <svg 
          v-if="state == 1"
          width="36" 
          height="15" 
          viewBox="0 0 36 15" 
          fill="none" 
          xmlns="http://www.w3.org/2000/svg"
          class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-4"
        >
          <path d="M19.139 14.2109C18.4538 14.6856 17.5462 14.6856 16.861 14.2109L1.60902 3.64399C-0.00241089 2.52756 0.787617 0 2.748 0L33.252 0C35.2124 0 36.0024 2.52756 34.391 3.64399L19.139 14.2109Z" fill="#011627"/>
        </svg>
      </div>
      <div 
        class="font-bold text-center border-b-4 -mb-1 relative flex flex-col justify-center gap-2"
        :class="`${ state == 2 ? 'border-black' : 'border-platinum'}`"
      >
        <p class="text-4xl">
          2
        </p>
        <p class="text-xxs lg:text-xl uppercase">
          Coordonnées
        </p>
        <svg 
          v-if="state == 2"
          width="36" 
          height="15" 
          viewBox="0 0 36 15" 
          fill="none" 
          xmlns="http://www.w3.org/2000/svg"
          class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-4"
        >
          <path d="M19.139 14.2109C18.4538 14.6856 17.5462 14.6856 16.861 14.2109L1.60902 3.64399C-0.00241089 2.52756 0.787617 0 2.748 0L33.252 0C35.2124 0 36.0024 2.52756 34.391 3.64399L19.139 14.2109Z" fill="#011627"/>
        </svg>
      </div>
      <div 
        class="font-bold text-center border-b-4 -mb-1 relative flex flex-col justify-center gap-2"
        :class="`${ state == 3 ? 'border-black' : 'border-platinum'}`"
      >
        <p class="text-4xl">
          3
        </p>
        <p class="text-xxs lg:text-xl uppercase">
          Paiement
        </p>
        <svg 
          v-if="state == 3"
          width="36" 
          height="15" 
          viewBox="0 0 36 15" 
          fill="none" 
          xmlns="http://www.w3.org/2000/svg"
          class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-4"
        >
          <path d="M19.139 14.2109C18.4538 14.6856 17.5462 14.6856 16.861 14.2109L1.60902 3.64399C-0.00241089 2.52756 0.787617 0 2.748 0L33.252 0C35.2124 0 36.0024 2.52756 34.391 3.64399L19.139 14.2109Z" fill="#011627"/>
        </svg>
      </div>
      <div 
        class="font-bold text-center border-b-4 border-maastricht-blue -mb-1 relative flex flex-col justify-center gap-2"
        :class="`${ state == 4 ? 'border-black' : 'border-platinum'}`"
      >
        <p class="text-4xl">
          4
        </p>
        <p class="text-xxs lg:text-xl uppercase">
          Confirmation
        </p>
        <svg 
          v-if="state == 4"
          width="36" 
          height="15" 
          viewBox="0 0 36 15" 
          fill="none" 
          xmlns="http://www.w3.org/2000/svg"
          class="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-4"
        >
          <path d="M19.139 14.2109C18.4538 14.6856 17.5462 14.6856 16.861 14.2109L1.60902 3.64399C-0.00241089 2.52756 0.787617 0 2.748 0L33.252 0C35.2124 0 36.0024 2.52756 34.391 3.64399L19.139 14.2109Z" fill="#011627"/>
        </svg>
      </div>
    </div>


    <div 
      v-if="state == 1"
      class="px-2 md:px-4 lg:px-16 xl:px-32" 
    >
      <div class="grid grid-cols-5 border-b-2 h-24 text-md lg:text-xl items-end pb-2">
        <p class="col-span-3">
          Bilet
        </p>
        <p class="col-span-1">
          Prix
        </p>
        <p class="col-span-1 text-right">
          Quantité
        </p>
      </div>
      <div class="grid grid-cols-5 h-24 items-center pb-2">
        <p class="col-span-3">
          <b>FLORENCE FORESTI</b> - Grand Théâtre - 26/06/2023
        </p>
        <p class="font-bold">
          63,00€
        </p>
        <select 
          name="" 
          id=""          
          class="border-2 border-maastricht-blue rounded-full w-12 lg:w-24 ml-auto px-2 py-1 font-bold"
        >
          <option value="1">
            1
          </option>
          <option value="2">
            2
          </option>
          <option value="3">
            3
          </option>
          <option value="4">
            4
          </option>
          <option value="5">
            5
          </option>
        </select>
      </div>
      <div class="bg-maximum-blue-green h-24 uppercase text-4xl font-bold flex justify-between items-center px-6">
        <p class="text-maastricht-blue ">
          Total
        </p>
        <p>
          63,00€
          <span class="font-normal">
            TTC
          </span>
        </p>
      </div>
      <div class="min-h-[6rem] flex flex-col xl:flex-row gap-5 lg:justify-between items-center p-6">
        <div class="space-y-2 lg:space-y-0 lg:gap-2 lg:flex items-center">
          <p class="text-xl font-bold">
            Code Pomosionnel :
          </p>
          <div class="flex flex-row">
            <input 
              type="text" 
              class="px-5 py-1 pr-7 border-2 border-maastricht-blue rounded-l-full outline-none" 
            >
            <p class="button-bg-secondary-two bg-white hover:border-black -ml-5 hover:bg-black">
              APPLIQUER
            </p>
          </div>
        </div>
        <div class="flex gap-6">
          <NuxtLink
            to="/"
            class="button-bg-secondary-two hover:border-maastricht-blue"
          >
            CONTINUER MES ACHATS
          </NuxtLink>
          <button @click="state++" class="button-bg-secondary-two bg-maastricht-blue text-white hover:bg-white hover:border-maastricht-blue hover:text-maastricht-blue">
            ÉTAPE SUIVANTE
          </button>
        </div>
      </div>
    </div>

    <div 
      v-if="state == 2"
      class="lg:text-xl"
    >
      <div class="bg-platinum py-6 px-2 md:px-4 lg:px-16 xl:px-32">
        <p>
          Merci de bien remplir les informations demandées. Vous recevrez un e-mail de confirmation.<br>
          Une pièce d'identité pourra vous être demandée à l'entrée de l'événement.
        </p>
      </div>
      <div class="grid sm:grid-cols-2 py-4 px-2 md:px-4 lg:px-16 xl:px-32 gap-6">
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="nom"
            class="text-xl"
          >
            Nom*
          </label>
          <input 
            id="nom" 
            class="px-5 py-1 border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="prenom"
            class="text-xl"
          >
            Prénom*
          </label>
          <input 
            id="prenom" 
            class="px-5 py-1 border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="email"
            class="text-xl"
          >
            Adresse email*
          </label>
          <input 
            id="email" 
            class="px-5 py-1 border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="re-email"
            class="text-xl"
          >
            Confirmation adresse email*
          </label>
          <input 
            id="re-email" 
            class="px-5 py-1 border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="zipcode"
            class="text-xl"
          >
            Code postal
          </label>
          <input 
            id="zipcode" 
            class="px-5 py-1 border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="space-y-2 lg:space-y-4">
          <label 
            for="tel"
            class="text-xl"
          >
            Numéro de téléphone
          </label>
          <input 
            id="tel" 
            class="px-5 py-1  border-2 border-maastricht-blue rounded-full outline-none w-full" 
            type="text"
          >
        </div>
        <div class="flex gap-3 lg:col-span-2">
          <input 
            id="new_infos"
            type="checkbox" 
            name="" 
          >
          <label for="new_infos">J'accepte de recevoir les informations du festival et de l'organisateur</label>
        </div>
        <div class="flex gap-3 lg:col-span-2">
          <input 
            id="cgv"
            type="checkbox" 
            name="" 
          >
          <label for="cgv">
            J'accepte les 
            <NuxtLink to="/cgv">
              conditions générales de vente
            </NuxtLink>
          </label>
        </div>
        <p>
          *les champs marqués d'une étoile sont obligatoires
        </p>
      </div>
      <div class="py-6 px-2 lg:px-32 flex flex-row-reverse gap-6">
        <button @click="state++" class="button-bg-secondary-two bg-maastricht-blue text-white hover:bg-white hover:border-maastricht-blue hover:text-maastricht-blue">
          ÉTAPE SUIVANTE
        </button>
        <button @click="state--" class="button-bg-secondary-two hover:border-maastricht-blue">
          ÉTAPE PRÉCÉDENTE
        </button>
      </div>
    </div>

    <div 
      v-if="state == 3"
      class="px-2 md:px-4 lg:px-16 xl:px-32" 
    >
      <div class="grid grid-cols-5 border-b-2 h-24 text-md lg:text-xl items-end pb-2">
        <p class="col-span-3">
          Bilet
        </p>
        <p class="col-span-1">
          Prix
        </p>
        <p class="col-span-1 text-right">
          Quantité
        </p>
      </div>
      <div class="grid grid-cols-5 h-24 items-center pb-2">
        <p class="col-span-3">
          <b>FLORENCE FORESTI</b> - Grand Théâtre - 26/06/2023
        </p>
        <p class="font-bold">
          63,00€
        </p>
        <select 
          name="" 
          id=""          
          class="border-2 border-maastricht-blue rounded-full w-12 lg:w-24 ml-auto px-2 py-1 font-bold"
        >
          <option value="1">
            1
          </option>
          <option value="2">
            2
          </option>
          <option value="3">
            3
          </option>
          <option value="4">
            4
          </option>
          <option value="5">
            5
          </option>
        </select>
      </div>
      <div class="bg-maximum-blue-green h-24 uppercase text-4xl font-bold flex justify-between items-center px-6">
        <p class="text-maastricht-blue ">
          Total
        </p>
        <p>
          63,00€
          <span class="font-normal">
            TTC
          </span>
        </p>
      </div>
      <div class="my-12 space-y-4">
        <p class="uppercase font-bold text-xl">
          VISA - MASTERCARD - CB
        </p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-9 gap-6">
          <div class="space-y-2 lg:space-y-4 lg:col-span-3">
            <label 
              for="card-nb"
              class="text-xl"
            >
              Numéro de carte*
            </label>
            <input 
              id="card-nb" 
              class="px-5 py-1  border-2 border-maastricht-blue rounded-full outline-none w-full" 
              type="text"
            >
          </div>
          <div class="space-y-2 lg:space-y-4 lg:col-span-2">
            <label 
              for="end-date"
              class="text-xl"
            >
              Date d'expiration*
            </label>
            <input 
              id="end-date" 
              class="px-5 py-1  border-2 border-maastricht-blue rounded-full outline-none w-full" 
              type="text"
            >
          </div>
          <div class="space-y-2 lg:space-y-4 lg:col-span-2">
            <label 
              for="cvv"
              class="text-xl"
            >
              CVC / CVV*
            </label>
            <input 
              id="cvv" 
              class="px-5 py-1  border-2 border-maastricht-blue rounded-full outline-none w-full" 
              type="text"
            >
          </div>
          <button 
            class="button-bg-secondary-two mt-auto w-full lg:col-span-2 bg-maastricht-blue text-white hover:bg-white hover:border-maastricht-blue hover:text-maastricht-blue"
            @click="state++" 
          >
            PAYER PAR CARTE
          </button>
        </div>
        <p>
          *les champs marqués d'une étoile sont obligatoires
        </p>
      </div>
      <hr>
      <div class="py-6 flex items-center justify-between">
        <p class="uppercase font-bold text-xl">PAYPAL</p>
        <button class="button-bg-secondary-two hover:border-maastricht-blue">
          Payer avec PAYPAL
        </button>
      </div>
      <!-- <div class="py-6 px-2 lg:px-32 flex flex-row-reverse gap-6">
        <button @click="state--" class="button-bg-secondary-two hover:border-maastricht-blue">
          ÉTAPE PRÉCÉDENTE
        </button>
      </div> -->
    </div>
    <div class="bg-platinum h-48 flex flex-col justify-center items-center gap-6">
      <p class="underline lg:text-xl uppercase font-bold">
        paiement sécurisé
      </p>
      <img src="@/src/icone_paiement.svg" alt="">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      state: 1,
    };
  }
};
</script>

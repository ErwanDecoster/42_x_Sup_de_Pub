<template>
  <div>
    <section class="background w-full px-6 h-[100vh]">
      <!-- <img
        class="h-2/5 absolute -right-20 -top-2 -rotate-90"
        src="@/src/halfcircle.svg"
        alt=""
      > -->
      <div class="mx-auto max-w-screen-2xl z-10 pt-[60vh] grid gap-6">
        <p class="text-white">
          <NuxtLink
            to="/"
            class="font-bold underline"
          >
            Acceuil
          </Nuxtlink> > Programmation & Billetterie
        </p>
        <h1 class="uppercase text-5xl lg:text-8xl text-khaki font-bold w-3/4">
          PROGRAMMATION & BILLETTERIE
        </h1>
      </div>
    </section>
    <section class="px-6">
      <div class="flex gap gap-6 flex-wrap py-6 md:py-16 mx-auto max-w-screen-2xl">
        <button 
          class="border-2 border-alizarin-crimson lg:text-2xl uppercase font-bold px-6 py-2 cursor-pointer"
          :class="`${ allFiltred ? 'bg-alizarin-crimson text-white' : 'bg-transparent text-alizarin-crimson' }`"
          @click="AllFilterState()"
        >
          Tout
        </button>
        <button 
          v-for="program in programs" 
          :key="program"
          class="border-2 border-alizarin-crimson lg:text-2xl uppercase font-bold px-6 py-2 cursor-pointer"
          :class="`${ program.filtred ? 'bg-transparent text-alizarin-crimson' : 'bg-alizarin-crimson text-white' }`"
          @click="program.filtred = !program.filtred; AllFilterStateFalse()"
        >
          {{ program.name }}
        </button>
      </div>
    </section>
    <section class="bg-maximum-blue-green py-12">
      <div class="mx-auto max-w-screen-2xl flex justify-between items-center px-6">
        <button class="w-11 h-11 border-2 border-maastricht-blue rounded-full flex items-center justify-center relative">
          <svg 
            width="18" 
            height="16" 
            viewBox="0 0 18 16" 
            fill="none" 
            xmlns="http://www.w3.org/2000/svg"
            class="scale-125"
          >
            <path 
              d="M16.6665 9C17.2188 9 17.6665 8.55228 17.6665 8C17.6665 7.44772 17.2188 7 16.6665 7V9ZM0.626062 7.29289C0.235538 7.68342 0.235538 8.31658 0.626062 8.70711L6.99002 15.0711C7.38055 15.4616 8.01371 15.4616 8.40424 15.0711C8.79476 14.6805 8.79476 14.0474 8.40424 13.6569L2.74738 8L8.40424 2.34315C8.79476 1.95262 8.79476 1.31946 8.40424 0.928932C8.01371 0.538408 7.38055 0.538408 6.99002 0.928932L0.626062 7.29289ZM16.6665 7L1.33317 7V9H16.6665V7Z" 
              fill="#011627"
            />
          </svg>
        </button>
        <div class="grid grid-cols-5 gap-4 lg:gap-12 uppercase">
          <div class="space-y-1">
            <p class="text-sm truncate w-7 sm:w-auto text-clip sm:text-xl">
              Lundi
            </p>
            <p class="text-2xl sm:text-7xl font-bold">
              31
            </p>
            <p class="text-sm sm:text-xl font-bold">
              MAI
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-sm truncate w-7 sm:w-auto text-clip sm:text-xl">
              Mardi
            </p>
            <p class="text-2xl sm:text-7xl font-bold">
              01
            </p>
            <p class="text-sm sm:text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-sm truncate w-7 sm:w-auto text-clip sm:text-xl">
              Mercredi
            </p>
            <p class="text-2xl sm:text-7xl font-bold">
              02
            </p>
            <p class="text-sm sm:text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-sm truncate w-7 sm:w-auto text-clip sm:text-xl">
              Jeudi
            </p>
            <p class="text-2xl sm:text-7xl font-bold">
              03
            </p>
            <p class="text-sm sm:text-xl font-bold">
              JUIN
            </p>
          </div>
          <div class="space-y-1">
            <p class="text-sm truncate w-7 sm:w-auto text-clip sm:text-xl">
              Vendredi
            </p>
            <p class="text-2xl sm:text-7xl font-bold">
              04
            </p>
            <p class="text-sm sm:text-xl font-bold">
              JUIN
            </p>
          </div>
        </div>
        <button class="w-11 h-11 border-2 border-maastricht-blue rounded-full flex items-center justify-center relative">
          <svg 
            width="18" 
            height="16" 
            viewBox="0 0 18 16" 
            fill="none" 
            xmlns="http://www.w3.org/2000/svg"
            class="scale-125 rotate-180"
          >
            <path 
              d="M16.6665 9C17.2188 9 17.6665 8.55228 17.6665 8C17.6665 7.44772 17.2188 7 16.6665 7V9ZM0.626062 7.29289C0.235538 7.68342 0.235538 8.31658 0.626062 8.70711L6.99002 15.0711C7.38055 15.4616 8.01371 15.4616 8.40424 15.0711C8.79476 14.6805 8.79476 14.0474 8.40424 13.6569L2.74738 8L8.40424 2.34315C8.79476 1.95262 8.79476 1.31946 8.40424 0.928932C8.01371 0.538408 7.38055 0.538408 6.99002 0.928932L0.626062 7.29289ZM16.6665 7L1.33317 7V9H16.6665V7Z" 
              fill="#011627"
            />
          </svg>
        </button>
      </div>
    </section>
    <section class="">
      <div 
        v-if="allFiltred"
        class="mx-auto max-w-screen-2xl text-white py-20 px-6"
      >
        <p class="w-full text-center text-xl">
          Aucun résultat ne correspond à votre recherche
        </p>
      </div>
      <div
        v-for="program in programs"
        :key="program"
        class="py-4 pt-16 px-6 grid gap-16 mx-auto group relative odd:bg-yankees-blue"
        :class="`${ program.filtred ? 'hidden' : 'block' }`"
      >
        <div class="mx-auto max-w-screen-2xl grid gap-16 relative w-full">
          <h2 class="text-7xl text-khaki uppercase font-bold">
            {{ program.name }}
          </h2>
          <div class="flex gap-12 overflow-x-scroll relative snap-x">
            <div
              v-for="show in program.shows"
              :key="show"
              class="grid gap-7 h-min min-w-[320px] w-80 snap-start"
            >
              <div class="relative">
                <img 
                  :src="`/${show.imgs[0].url}.jpeg`" 
                  alt=""
                  class="h-80 w-80 bg-black object-cover"
                >
                <div class="bg-maastricht-blue group-odd:bg-yankees-blue absolute bottom-0 left-0 h-24 w-24 rounded-tr-full text-white">
                  <p class="absolute bottom-3 left-3 text-3xl">
                    {{ show.price }}€
                  </p>
                </div>
              </div>
              <div class="flex justify-between items-center">
                <p class="text-xl font-bold text-white shrink">
                  {{ show.author }}
                </p>
                <button class="button-secondary w-36">
                  Voir plus
                </button>
              </div>
              <div class="relative z-10 h-44">
                <button 
                  class="button-primary-two w-full hover:bg-maastricht-blue group-odd:hover:bg-yankees-blue absolute"
                  @click="show.book = ! show.book" 
                >
                  Réserver
                </button>
                <div 
                  v-if="show.book"
                  class="p-4 space-y-4 absolute bg-zomp right-0 left-0 top-0 pt-14 -z-10 rounded-3xl"
                >
                  <select 
                    id=""
                    name="" 
                    class="w-full z-30 border-2 border-maastricht-blue group-odd:border-yankees-blue bg-maastricht-blue group-odd:bg-yankees-blue text-white rounded-full px-2 py-1 font-bold"
                  >
                    <option value="select">
                      DATE
                    </option>
                    <option 
                      v-for="date in show.dates"
                      :key="date"
                      :value="date.time"
                    >
                      {{ date.time }}
                    </option>
                  </select>
                  <div class="flex justify-between">
                    <select 
                      id=""
                      name="" 
                      class="border-2 border-maastricht-blue group-odd:border-yankees-blue bg-maastricht-blue group-odd:bg-yankees-blue text-white rounded-full px-2 py-1 font-bold"
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
                    <button class="button-primary">
                      Panier
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div 
            class="absolute mt-0 z-10 right-0 bottom-2 w-20 h-[610px] bg-gradient-to-r from-transparent to-maastricht-blue group-odd:to-yankees-blue" 
            :class="`${ program.shows.length <= 4 ? '2xl:hidden' : 'block' }`"
          />
          <div class="flex gap-2 items-center absolute bottom-4 right-4 z-10">
            <p class="text-white text-lg">
              <b>1-{{ program.shows.length }}</b> 
              sur 
              <b>{{ program.shows.length }}</b>
            </p>
            <button class="w-11 h-11 border-2 border-white rounded-full flex items-center justify-center relative">
              <svg 
                width="18" 
                height="16" 
                viewBox="0 0 18 16" 
                fill="none" 
                xmlns="http://www.w3.org/2000/svg"
                class="scale-125"
              >
                <path 
                  d="M16.6665 9C17.2188 9 17.6665 8.55228 17.6665 8C17.6665 7.44772 17.2188 7 16.6665 7V9ZM0.626062 7.29289C0.235538 7.68342 0.235538 8.31658 0.626062 8.70711L6.99002 15.0711C7.38055 15.4616 8.01371 15.4616 8.40424 15.0711C8.79476 14.6805 8.79476 14.0474 8.40424 13.6569L2.74738 8L8.40424 2.34315C8.79476 1.95262 8.79476 1.31946 8.40424 0.928932C8.01371 0.538408 7.38055 0.538408 6.99002 0.928932L0.626062 7.29289ZM16.6665 7L1.33317 7V9H16.6665V7Z" 
                  fill="white"
                />
              </svg>
            </button>
            <button class="w-11 h-11 border-2 border-white rounded-full flex items-center justify-center relative">
              <svg 
                width="18" 
                height="16" 
                viewBox="0 0 18 16" 
                fill="none" 
                xmlns="http://www.w3.org/2000/svg"
                class="scale-125 rotate-180"
              >
                <path 
                  d="M16.6665 9C17.2188 9 17.6665 8.55228 17.6665 8C17.6665 7.44772 17.2188 7 16.6665 7V9ZM0.626062 7.29289C0.235538 7.68342 0.235538 8.31658 0.626062 8.70711L6.99002 15.0711C7.38055 15.4616 8.01371 15.4616 8.40424 15.0711C8.79476 14.6805 8.79476 14.0474 8.40424 13.6569L2.74738 8L8.40424 2.34315C8.79476 1.95262 8.79476 1.31946 8.40424 0.928932C8.01371 0.538408 7.38055 0.538408 6.99002 0.928932L0.626062 7.29289ZM16.6665 7L1.33317 7V9H16.6665V7Z" 
                  fill="white"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      allFiltred: false,
      programs: [
        {
          filtred: false,
          name: "têtes d'affiche",
          shows: [
            {
              author: "FLORENCE FORESTI",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "florence_foresti",
                },
                {
                  size: 'small',
                  url: "florence_foresti",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MICHEL POLNAREFF",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "michel_polnareff",
                },
                {
                  size: 'small',
                  url: "michel_polnareff",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "CHRISTINE AND THE QUEENS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "christine_and_the_queens",
                },
                {
                  size: 'small',
                  url: "christine_and_the_queens",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BENJAMIN BIOLAY",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "benjamin_biolay",
                },
                {
                  size: 'small',
                  url: "benjamin_biolay",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
        {
          filtred: false,
          name: "MUSIQUE",
          shows: [
            {
              author: "MICHEL POLNAREFF",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "michel_polnareff",
                },
                {
                  size: 'small',
                  url: "michel_polnareff",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "CHRISTINE AND THE QUEENS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "christine_and_the_queens",
                },
                {
                  size: 'small',
                  url: "christine_and_the_queens",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BENJAMIN BIOLAY",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "benjamin_biolay",
                },
                {
                  size: 'small',
                  url: "benjamin_biolay",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "THE BLACK KEYSE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "the_black_keyse",
                },
                {
                  size: 'small',
                  url: "the_black_keyse",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },

        {
          filtred: false,
          name: "THÉÂTRE",
          shows: [
            {
              author: "SORCIÈRES",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "sorcieres",
                },
                {
                  size: 'small',
                  url: "sorcieres",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "ISABELLE ADJANI",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "isabelle_adjani",
                },
                {
                  size: 'small',
                  url: "isabelle_adjani",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "LE BEAU MONDE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "le_beau_monde",
                },
                {
                  size: 'small',
                  url: "le_beau_monde",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "COMP. MARIUS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "comp_marius",
                },
                {
                  size: 'small',
                  url: "comp_marius",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },

        {
          filtred: false,
          name: "CIRQUE",
          shows: [
            {
              author: "BALESTRA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "balestra",
                },
                {
                  size: 'small',
                  url: "balestra",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BARO D'EVEL",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "baro_d_evel",
                },
                {
                  size: 'small',
                  url: "baro_d_evel",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "NOFIT STATE CIRCUS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "nofit_state_circus",
                },
                {
                  size: 'small',
                  url: "nofit_state_circus",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
        {
          filtred: false,
          name: "DANSE",
          shows: [
            {
              author: "COMPAGNIE DCA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "compagnie_dca",
                },
                {
                  size: 'small',
                  url: "compagnie_dca",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "BEYTNA",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "beytna",
                },
                {
                  size: 'small',
                  url: "beytna",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MEHDI KERKOUCHE",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "mehdi_kerkouche",
                },
                {
                  size: 'small',
                  url: "mehdi_kerkouche",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
            {
              author: "MARÍA PAGÉS",
              book: false,
              price: 25,
              imgs: [
                {
                  size: 'large',
                  url: "maria_pages",
                },
                {
                  size: 'small',
                  url: "maria_pages",
                },
              ],
              dates: [
                {
                  time: "25/04/2023 21:45:00",
                },
                {
                  time: "26/04/2023 21:45:00",
                },
                {
                  time: "27/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "28/04/2023 21:45:00",
                },
                {
                  time: "30/04/2023 21:45:00",
                },
              ]
            },
          ]
        },
      ],
    };
  },
  methods: {
    AllFilterStateFalse() {
      let count = 0;
      for (let i = 0; i < this.programs.length; i++) {
        if (this.programs[i].filtred == false)
          count++;
      }
      if (count == this.programs.length) {
        console.log(count, false);
        this.allFiltred = false;
      }
      else if (count == 0) {
        this.allFiltred = true;
      } else {
        this.allFiltred = false;
      }
    },
    AllFilterState() {
      const majority = !this.MajorityState();
      for (let i = 0; i < this.programs.length; i++) {
        this.programs[i].filtred = majority;
      }
      this.allFiltred = majority;
    },
    MajorityState() {
      console.log(this.programs);
      let count = 0;
      for (let i = 0; i < this.programs.length; i++) {
        if (this.programs[i].filtred == true)
          count++;
      }
      if (count >= this.programs.length / 2)
        return true;
      return false;
    },
  }
};
</script>
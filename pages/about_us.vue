<template>
  <div>
    <section class="background w-full h-[95vh]">
      <!-- <img
        class="h-2/5 absolute -right-20 -top-2 -rotate-90"
        src="@/src/halfcircle.svg"
        alt=""
      > -->
      <div class="z-10 pt-[60vh] px-8 grid gap-6">
        <p class="text-white">
          <NuxtLink
            to="/"
            class="font-bold"
          >
            Acceuil
          </Nuxtlink> > Qui somme-nous ?
        </p>
        <h1 class="uppercase text-8xl text-khaki font-bold w-3/4">
          Qui somme nous ?
        </h1>
      </div>
    </section>
    <section class="w-full bg-[#1a2d3d]">
      <div class="py-24 px-6 max-w-screen-2xl mx-auto">
        <p class="whitespace-nowrap text-white text-5xl font-bold pb-12">
          CHIFFRES CLÉS
        </p>
        <div class="grid m-auto md:grid-cols-2 sm:grid-cols-1 xl:grid-cols-4 justify-between gap-6">
          <div class="w-56">
            <p class="text-white text-base font-normal pb-5">
              Date de création
            </p>
            <p class="text-white text-4xl text-bold">
              1946
            </p>
          </div>
          <div class="w-56">
            <p class="text-white text-base font-normal pb-5">
              Représentations / édition
            </p>
            <p class="text-white text-4xl text-bold">
              > 150
            </p>
          </div>
          <div class="w-56">
            <p class="text-white text-base font-normal pb-5">
              Spectateurs / édition
            </p>
            <p class="text-white text-4xl text-bold">
              >150 000
            </p>
          </div>
          <div class="w-56">
            <p class="text-white text-base font-normal pb-5">
              Fréquentation moyenne
            </p>
            <p class="text-white text-4xl text-bold">
              83%
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="flex flex-col max-w-screen-2xl mx-auto gap-24 py-24">
      <div class="grid justify-center xl:grid-cols-5 w-full xl:gap-36 gap-6 p-6">
        <div class="flex flex-col gap-6 xl:order-1 xl:col-span-3">
          <img 
            class="w-auto md:max-w-4xl"
            src="@/src/image_1.png"
            alt=""
          >
          <p class="text-white text-base font-normal italic">
            Édition 2022 des Nuits de Fourvière
          </p>
        </div>
        <div class="flex flex-col gap-12 xl:col-span-2">
          <div>
            <p class="text-white font-normal text-2xl md:text-4xl">
              LES ARTS DE LA SCÈNE
            </p>
            <p class="text-khaki font-bold text-3xl -mt-5 md:text-5xl">
              MULTIDISCIPLINARITÉ
            </p>
          </div>
          <div class="flex flex-col gap-6">
            <p class="text-white text-base font-normal md:max-w-3xl">
              Théâtre, musique, danse, opéra, cirque... Les Nuits de Fourvière sont dévolues aux arts de la scène et s'attachent, 
              depuis 1946, à faire coexister les disciplines. Chaque été, en juin et juillet, le festival présente plus de 150 
              représentations pour plus de 150000 spectateurs. Si la pluridisciplinarité est un critère, elle n'est en rien une 
              règle absolue. Le festival garantit son ouverture et sa modernité en se gardant de normer ou de thématiser. 
              Les Nuits se sont sculptées un projet artistique singulier avec pour seule boussole la qualité artistique des 
              projets et leur inscription sur la scène internationale.
            </p>
            <NuxtLink class="button-primary-two">
              TOUTE LA PROGRAMMATION
            </NuxtLink>
          </div>
          <div class="md:max-w-3xl">
            <div class="flex flex-col pl-20 gap-6">
              <p class="text-white text-base font-normal">
                D'année en année, sous l'impulsion de son directeur, Dominique Delorme, le festival Les Nuits de Fourvière 
                affirme sa fringale d'audace et d'originalité car derrière les arbres de passage conventionnel c'est bien 
                une forêt d'initiatives qui, deux mois durant, constelle une programmation faisant feu de tout bois 
                (theatre, classique, danse, rock, world...)
              </p>
              <p class="text-white text-base font-normal">
                Libération, 2010
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="grid justify-center xl:grid-cols-5 w-full xl:gap-36 gap-6 p-6">
        <div class="flex flex-col gap-6 xl:order-1 xl:col-span-3">
          <img 
            class="w-auto md:max-w-4xl"
            src="@/src/image_2.png" 
            alt=""
          >
          <p class="text-white text-base font-normal italic">
            Édition 2022 des Nuits de Fourvière
          </p>
        </div>
        <div class="flex flex-col gap-12 xl:col-span-2">
          <div class="flex flex-col gap-6">
            <p class="text-white font-bold text-2xl md:text-4xl">
              ACCUEIL SOIGNÉ,<br>PUBLIC CHALEUREUX
            </p>
            <p class="text-white text-base font-normal md:max-w-3xl">
              Les Nuits rassemblent chaque été plus de 130 000 spectateurs. La politique tarifaire permet l'accès à un 
              large public. La fréquentation moyenne est de 83%.
            </p>
          </div>
          <div class="flex flex-col gap-6">
            <p class="text-white font-bold text-2xl md:text-4xl">
              RÉSEAU MONDIAL
            </p>
            <p class="text-white text-base font-normal md:max-w-3xl">
              À chacune de leurs éditions, Les Nuits de Fourvière produisent ou coproduisent des créations de dimension 
              internationale, en partenariat avec des institutions et festivals comme le Barbican Centre et le Sadler's 
              Wells à Londres, le Théâtre de la Ville à Paris, le Théâtre des Bouffes du Nord, le Lincoln Center 
              Festival à New York, le festival d'Athènes, le festival El Grec à Barcelone, les Théâtres de la Ville de 
              Luxembourg, le Théâtre de la Place à Liège... Sous l'appellation NUITS, une partie de la programmation du 
              festival se consacre à des artistes du monde entier : Bénin (Nuit au Bénin), Espagne (Nuit du Flamenco), 
              Bali, Argentine (Nuit Tango), Pékin (Opéra de Pékin)...
            </p>
          </div>
        </div>
      </div>

      <div class="grid justify-center xl:grid-cols-5 w-full xl:gap-36 gap-6 p-6">
        <div class="flex flex-col gap-6 xl:col-span-3">
          <img 
            class="w-auto md:max-w-4xl"
            src="@/src/image_3.png" 
            alt=""
          >
          <p class="text-white text-base font-normal italic">
            Édition 2022 des Nuits de Fourvière
          </p>
        </div>
        <div class="flex flex-col gap-12 xl:col-span-2">
          <div>
            <p class="text-white font-normal text-2xl md:text-4xl">
              LE SITE DE FOURVIÈRE
            </p>
            <p class="text-khaki font-bold text-3xl -mt-5 md:text-5xl">
              UN LIEU UNIQUE
            </p>
          </div>
          <div class="flex flex-col gap-6">
            <p class="text-white text-base font-normal md:max-w-3xl">
              La recherche du site antique fut, longtemps, une des questions centrales de l'archéologie lyonnaise. 
              Pour tenter d'y répondre, Edouard Herriot, alors Maire de Lyon, amorce un chantier de fouille en 1933. 
              Contraintes pendant la guerre, ces fouilles ressuscitent le Grand théâtre en 1946. Herriot l'inaugure 
              le 29 juin. À l'issue d'un discours mémorable, on présente Les Perses d'Eschyle par le Groupe de Théâtre 
              Antique de la Sorbonne. Le petit Odéon fait son entrée en scène le 25 juin 1952 avec Les Concertos 
              Brandebourgeois sous la direction de Karl Münchinger. Faire revivre le site, l'animer en présentant des 
              spectacles est donc, dès le départ, un rêve absolu et une ambition partagée. Personne ne songe alors à 
              appeler festival cette nouvelle rencontre entre la cité et les artistes qui précède d'un an la première 
              semaine d'art d'Avignon. Depuis le festival n'a cessé de réunir chaque été la population autour d'un 
              programme artistique populaire et de renommée internationale. Le site arbore, en plein cœur de Lyon, 
              deux espaces contigus : le Grand théâtre (4400 places) et l'Odéon (1200 places).
            </p>
            <NuxtLink class="button-primary-two">
              COMMENT VENIR
            </NuxtLink>
          </div>
          <div class="md:max-w-3xl">
            <div class="flex flex-col pl-20 gap-6">
              <p class="text-white text-base font-normal">
                Les Nuits de Fourvière ont plusieurs atouts. Le site d'abord : la bucolique colline de Fourvière 
                qui domine Lyon, et où les Romains ont fondé Lugdunum.
              </p>
              <p class="text-white text-base font-normal">
                Le Monde, 2010
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<template>
  
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
  <router-link
          :to="{ name: 'home' }"
          class="navbar-brand"
        >Question Time
        </router-link>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <router-link
          :to="{ name: 'home' }"
          class="btn btn-sm"
        >Home
        </router-link>
      </li>
      <li class="nav-item">
        <router-link
          :to="{ name: 'about' }"
          class="btn btn-sm"
        >About
        </router-link>
      </li>
      <li class="nav-item">
        <router-link
          :to="{ name: 'about' }"
          class="btn btn-sm"
        >About
        </router-link>
      </li>
      <li class="nav-item">
        <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/">Logout</a>
      </li>
    </ul>
  </div>
  </div>
</nav>
</template>

<script>

export default {
  name:"NavbarComponent"
}

</script>

<style>

</style>

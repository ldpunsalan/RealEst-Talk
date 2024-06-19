<div class="card">
  <slot></slot>
</div>

<style>
  .card {
    background-image: radial-gradient(circle at center, #ffffff2b, #11111b7a);
    border-radius: 15px;
    padding: 40px 50px;
    margin: 10px 10px;
    position: relative;
    border: 1px solid transparent;
    background:
      linear-gradient(#1e1e2e 0 0) padding-box padding-box,
      linear-gradient(to right, #cba6f7, #89b4fa) border-box;
  }
</style>

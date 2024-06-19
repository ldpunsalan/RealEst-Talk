<div class="card">
  <slot></slot>
</div>

<style>
  .card {
    border-radius: 15px;
    padding: 30px 30px;
    margin: 10px 10px;
    position: relative;
    border: 1px solid transparent;
    background:
      linear-gradient(#1e1e2e 0 0) padding-box padding-box,
      linear-gradient(to right, #cba6f7, #89b4fa) border-box;
  }
</style>

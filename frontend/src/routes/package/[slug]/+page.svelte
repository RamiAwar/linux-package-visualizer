<script>
	import Package from '$lib/Package.svelte';

	export let data;
</script>

<Package details={data.package_data} />

<script lang="ts">
	import type { Package } from '$lib/package';

	export let details: Package;
</script>

<div class=" bg-white overflow-hidden">
	<div class="mt-10 mb-5">
		<h2 class="text-lg font-medium text-gray-800">Package Metadata</h2>
		<dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2 md:grid-cols-3 mt-3">
			{#if details?.status}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Status</dt>
					<dd class="mt-1 text-sm text-gray-900">{details.status}</dd>
				</div>
			{/if}

			{#if details?.maintainer}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Maintainer</dt>
					<dd class="mt-1 text-sm text-gray-900">{details?.maintainer}</dd>
				</div>
			{/if}

			{#if details?.architecture}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Architecture</dt>
					<dd class="mt-1 text-sm text-gray-900">{details.architecture}</dd>
				</div>
			{/if}

			{#if details?.homepage}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Homepage</dt>
					<a href={details.homepage}><dd class="mt-1 text-sm text-gray-900">{details.homepage}</dd></a>
				</div>
			{/if}

			{#if details?.priority}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Priority</dt>
					<dd class="mt-1 text-sm text-gray-900">{details.priority}</dd>
				</div>
			{/if}

			{#if details?.section}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Section</dt>
					<dd class="mt-1 text-sm text-gray-900">{details.section}</dd>
				</div>
			{/if}

			{#if details?.installed_size}
				<div class="sm:col-span-1">
					<dt class="text-sm font-medium text-gray-500">Installed Size</dt>
					<dd class="mt-1 text-sm text-gray-900">{details.installed_size}</dd>
				</div>
			{/if}
		</dl>
	</div>
</div>

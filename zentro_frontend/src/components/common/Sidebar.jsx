// src/components/common/Sidebar.jsx
import React, { useEffect, useRef, useState } from "react";

/**
 * Sidebar: el icono de pesas actúa como toggle (expand/collapse en desktop, open/close en mobile)
 */
export default function Sidebar({
	activeSection,
	onNavigate,
	collapsed: controlledCollapsed,
	onToggle,
}) {
	const [localCollapsed, setLocalCollapsed] = useState(false);
	const [mobileOpen, setMobileOpen] = useState(false);
	const collapsed =
		typeof controlledCollapsed === "boolean" ? controlledCollapsed : localCollapsed;

	const rootRef = useRef();

	useEffect(() => {
		const handleClick = (e) => {
			if (!mobileOpen) return;
			if (rootRef.current && !rootRef.current.contains(e.target)) {
				setMobileOpen(false);
			}
		};
		document.addEventListener("mousedown", handleClick);
		return () => document.removeEventListener("mousedown", handleClick);
	}, [mobileOpen]);

	const navItems = [
		{ id: "dashboard", name: "Dashboard", icon: "fa-home", to: "/" },
		{ id: "clientes", name: "Clientes", icon: "fa-users", to: "/clientes" },
		{ id: "recepcion", name: "Recepción", icon: "fa-id-card", to: "/recepcion" },
		{ id: "membresias", name: "Membresías", icon: "fa-credit-card", to: "/membresias" },
		{ id: "clases", name: "Clases", icon: "fa-calendar-alt", to: "/clases" },
		{ id: "entrenadores", name: "Entrenadores", icon: "fa-user-tie", to: "/entrenadores" },
		{ id: "rutinas", name: "Rutinas", icon: "fa-clipboard-list", to: "/rutinas" },
		{ id: "nutricion", name: "Nutrición", icon: "fa-apple-alt", to: "/nutricion" },
		{ id: "tienda", name: "Tienda", icon: "fa-store", to: "/tienda" },
		{ id: "incidentes", name: "Incidentes", icon: "fa-exclamation-triangle", to: "/incidentes" },
		{
			id: "admin",
			name: "Administración",
			icon: "fa-cog",
		},
		{ id: "configuracion", name: "Configuración", icon: "fa-sliders-h", to: "/configuracion" },
		{ id: "ayuda", name: "Ayuda", icon: "fa-question-circle", to: "/ayuda" },
	];

	const handleToggle = () => {
		const next = !collapsed;
		if (typeof onToggle === "function") onToggle(next);
		if (typeof controlledCollapsed !== "boolean") setLocalCollapsed(next);
	};

	const handleNavigate = (it) => {
		if (typeof onNavigate === "function") {
			onNavigate(it.id);
			setMobileOpen(false);
			return;
		}
		if (it.to) {
			window.location.href = it.to;
			setMobileOpen(false);
			return;
		}
		window.history.pushState({}, "", `/${it.id}`);
		window.dispatchEvent(new CustomEvent("sidebar:navigate", { detail: { id: it.id } }));
		setMobileOpen(false);
	};

	function NavItem({ item }) {
		const isActive = activeSection === item.id;
		const hasChildren = Array.isArray(item.children);
		const [open, setOpen] = useState(false);

		useEffect(() => {
			if (hasChildren && item.children.some((c) => c.id === activeSection)) {
				setOpen(true);
			}
		}, [hasChildren, item.children]);

		return (
			<li>
				<div
					className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-colors duration-150
						${isActive ? "bg-gray-700 text-white shadow-sm" : "text-sidebar-muted hover:bg-sidebar-hover hover:text-white"}
						${collapsed ? "justify-center px-2 py-3" : "justify-start"}
					`}
					role="button"
					tabIndex={0}
					onClick={() => (hasChildren ? setOpen((s) => !s) : handleNavigate(item))}
					onKeyDown={(e) => {
						if (e.key === "Enter" || e.key === " ") {
							e.preventDefault();
							if (hasChildren) setOpen((s) => !s);
							else handleNavigate(item);
						}
					}}
					title={collapsed ? item.name : undefined}
					aria-expanded={hasChildren ? open : undefined}
				>
					<div className={`flex items-center justify-center ${collapsed ? "w-6 h-6" : "w-8 h-8"}`}>
						<i className={`fas ${item.icon} ${isActive ? "text-white" : "text-sidebar-icon-fore"} text-lg`} />
					</div>

					{!collapsed && <span className="text-lg font-medium truncate">{item.name}</span>}

					{!collapsed && hasChildren && (
						<i className={`fas fa-chevron-${open ? "up" : "down"} ml-auto text-sidebar-muted`} />
					)}
				</div>

				{hasChildren && open && (
					<ul className={`${collapsed ? "ml-0" : "ml-10"} mt-2 space-y-1`}>
						{item.children.map((c) => {
							const childActive = activeSection === c.id;
							return (
								<li key={c.id}>
									<button
										onClick={() => handleNavigate(c)}
										className={`flex items-center gap-3 w-full px-3 py-2 rounded-lg text-sm
											${childActive ? "bg-gray-700 text-white" : "text-sidebar-muted hover:bg-sidebar-hover hover:text-white"}
											${collapsed ? "justify-center" : "justify-start"}`}
										title={collapsed ? c.name : undefined}
									>
										<div className="w-7 h-7 flex items-center justify-center rounded-md">
											<i className={`fas ${c.icon} text-sm ${childActive ? "text-white" : "text-sidebar-icon-fore"}`} />
										</div>
										{!collapsed && <span className="truncate">{c.name}</span>}
									</button>
								</li>
							);
						})}
					</ul>
				)}
			</li>
		);
	}

	// helper: cuando se hace click sobre el logo/peso
	const handleBrandClick = () => {
		// si viewport lg en adelante -> toggle collapsed
		const isLarge = window.matchMedia("(min-width: 1024px)").matches;
		if (isLarge) {
			handleToggle();
		} else {
			// en móvil abrimos/cerramos drawer
			setMobileOpen((s) => !s);
		}
	};

	return (
		<>
			<div
				className={`fixed inset-0 z-30 lg:hidden transition-opacity ${mobileOpen ? "opacity-40 pointer-events-auto" : "opacity-0 pointer-events-none"}`}
				style={{ backgroundColor: "rgba(0,0,0,0.4)" }}
				onClick={() => setMobileOpen(false)}
				aria-hidden={!mobileOpen}
			/>

			<aside
				ref={rootRef}
				className={`fixed top-0 left-0 z-40 h-screen transform transition-transform duration-300
					${mobileOpen ? "translate-x-0" : "-translate-x-full"} lg:translate-x-0
					${collapsed ? "w-16" : "w-64"}
					bg-gradient-to-b from-[#071226] to-[#0b1724] text-white shadow-lg
				`}
				aria-label="Barra lateral principal"
			>
				<div className="h-full flex flex-col">
					{/* BRAND: el icono de pesas ahora es botón para toggle */}
					<div className={`p-4 ${collapsed ? "flex items-center justify-center" : ""} border-b border-[#0e1620]`}>
						<div className="flex items-center gap-3">
							<button
								onClick={handleBrandClick}
								title={collapsed ? "Mostrar menú" : "Colapsar/expandir sidebar"}
								aria-label={collapsed ? "Mostrar menú" : "Colapsar/expandir sidebar"}
								className={`w-10 h-10 rounded-lg flex items-center justify-center ${collapsed ? "mx-auto" : ""} bg-white/5 focus:outline-none focus:ring-2 focus:ring-indigo-500`}
							>
								<i className="fas fa-dumbbell text-white" aria-hidden="true" />
							</button>

							{!collapsed && (
								<div>
									<h1 className="text-lg font-semibold">Zentro</h1>
									<p className="text-xs text-sidebar-muted -mt-0.5">Control del gimnasio</p>
								</div>
							)}
						</div>
					</div>

					<nav className="flex-1 overflow-y-auto p-3 sidebar-scroll" role="navigation" aria-label="Menú principal">
						<ul className="space-y-2">
							{navItems.map((it) => (
								<NavItem key={it.id} item={it} />
							))}
						</ul>
					</nav>

					{/* FOOTER: eliminado botón colapsar y cerrar sesión. Solo Soporte/Acerca opcionales */}
					<div className="p-3 border-t border-[#0e1620]">
						{!collapsed && (
							<div className="mt-2 text-xs text-sidebar-muted">
								<button className="w-full text-left px-2 py-2 rounded hover:bg-gray-800">Soporte</button>
								<button className="w-full text-left px-2 py-2 rounded hover:bg-gray-800">Acerca</button>
							</div>
						)}
					</div>
				</div>
			</aside>
		</>
	);
}